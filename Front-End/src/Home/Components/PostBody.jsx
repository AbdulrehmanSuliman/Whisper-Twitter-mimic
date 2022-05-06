import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Carousel } from 'react-responsive-carousel';
import PropTypes from 'prop-types';
import ImagePopUp from './ImagePopUp';
import styles from './Post.module.css';
import ImageBox from './ImageBox';

function PostBody({
  id, content, URLs,
}) {
  const navigate = useNavigate();
  const [imagePopUp, setImagePopUp] = useState(false);
  const [images, setImages] = useState([]);
  useEffect(() => {
    const tempURLs = [...URLs];
    tempURLs.forEach((element, index) => {
      // eslint-disable-next-line no-param-reassign
      tempURLs[index] = {
        id: index,
        imageUrl: element,
      };
    });
    setImages(tempURLs);
  }, [URLs]);
  return (
    <div>
      <div
        data-testid="content-render-test"
        className={styles.postheaderdescription}
        role="button"
        tabIndex={0}
        onClick={() => navigate(`/tweet/${id}`)}
      >
        <p>{content}</p>
      </div>

      <div
        data-testid="images-render-test"
        role="button"
        tabIndex={0}
        onClick={() => setImagePopUp(!imagePopUp)}
      >
        <ImageBox images={images} deleteEnabled />
      </div>
      <div>
        {imagePopUp
              && document.getElementsByTagName('body')[0].style.setProperty('overflow-y', 'hidden')}
        {images[0] && (
        <ImagePopUp name="body" trigger={imagePopUp} setTrigger={setImagePopUp}>
          <Carousel>
            {images.map((element) => (
              <div key={element.id}>
                <img className={styles.imgpopup} src={element.imageUrl} alt="pic1" />
              </div>
            ))}
          </Carousel>
        </ImagePopUp>
        )}
      </div>
    </div>
  );
}

PostBody.propTypes = {
  id: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  URLs: PropTypes.arrayOf(PropTypes.string).isRequired,

};
export default PostBody;
