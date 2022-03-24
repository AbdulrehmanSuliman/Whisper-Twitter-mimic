import React, { createRef, useState } from 'react';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import PhotoOutlinedIcon from '@mui/icons-material/PhotoOutlined';
import GifBoxOutlinedIcon from '@mui/icons-material/GifBoxOutlined';

import request from 'superagent';
import ImageBox from './ImageBox';
import PopupPage from './PopupPage';
import SearchBar from './SearchBar';

import styles from './TweetBox.module.css';

function TweetBox() {
  const inputFile = createRef();
  const [images, setImages] = useState([]);
  const [imageCount, setImageCount] = useState(1);
  const [isGifOpen, setIsGifOpen] = useState(false);
  const [gifs, setGifs] = useState([]);

  const onSearchChange = (value) => {
    let url;
    if (value === '') {
      url = 'http://api.giphy.com/v1/gifs/trending?api_key=3Tq937jtd7Hyq33VveHBIZsJABFPz1vF';
    } else { url = `http://api.giphy.com/v1/gifs/search?q=${value}&api_key=3Tq937jtd7Hyq33VveHBIZsJABFPz1vF`; }
    request.get(url, (err, res) => {
      setGifs(res.body.data);
    });
  };
  const deleteImage = (id) => {
    const newImages = images.filter((image) => image.id !== id);
    setImages(newImages);
    setImageCount(imageCount - 1);
  };
  const autoGrow = (element) => {
    // eslint-disable-next-line no-param-reassign
    element.target.style.height = 'inherit';
    // eslint-disable-next-line no-param-reassign
    element.target.style.height = `${element.target.scrollHeight < 101 ? element.target.scrollHeight - 22 : element.target.scrollHeight}px`;
  };
  const onSelectFIle = () => {
    inputFile.current.click();
  };

  const handleFileInput = (event) => {
    if (event.target.files.length + imageCount - 1 > 4) {
      return;
    }
    const tempImages = [...images];
    let tempCounter = imageCount;
    if (event.target.files && event.target.files[0]) {
      Array.from(event.target.files).forEach((file) => {
        tempImages.push({
          id: tempCounter,
          imageUrl: URL.createObjectURL(file),
        });
        tempCounter += 1;
      });
      setImageCount(tempCounter);
      setImages(tempImages);
    }
  };

  const onOpenGif = () => {
    if (imageCount - 1 < 4) {
      document.getElementsByTagName('body')[0].style.setProperty('overflow', 'hidden');
      setIsGifOpen(!isGifOpen);
      onSearchChange('');
    }
  };

  const onSelectGif = (url) => {
    setImages([...images,
      {
        id: imageCount,
        imageUrl: url,
      }]);
    setImageCount(imageCount + 1);
    document.getElementsByTagName('body')[0].style.setProperty('overflow', 'scroll');
    setIsGifOpen(!isGifOpen);
  };
  return (
    <div>
      <PopupPage trigger={isGifOpen} SetTrigger={setIsGifOpen}>
        <div className={styles['inner-gif']}>
          <SearchBar searchValue={onSearchChange} placeHolder="Search for GIFs" />
          <div className={styles['popup-imgs-container']}>
            {gifs.map((gif) => ((gifs.length === 0) ? '' : (
              <div role="button" tabIndex={0} onClick={() => onSelectGif(gif.images.original.url)} key={gif.id}>
                <img className={styles['popup-img']} alt="" src={gif.images.original.url} />
              </div>
            )))}
          </div>
        </div>
      </PopupPage>

      <div className={styles['tweet-box']}>
        <a href="#top" className={styles['icon-button']}>
          <AccountCircleIcon className={styles.icon} />
        </a>
        <div className={styles['text-area']}>
          <div>
            <textarea placeholder="What's Happening?" className={styles['tweet-input']} onInput={autoGrow} />
          </div>
          <ImageBox images={images} onDeleteImage={deleteImage} />
          <div className={styles['text-area-icons']}>
            <div className={styles['media-icons']}>
              <div role="button" tabIndex="0" onClick={onSelectFIle}>
                <PhotoOutlinedIcon className={styles['media-icon']} />
                <input type="file" id="file" multiple="multiple" accept=".jpg, .png" ref={inputFile} onChange={handleFileInput} style={{ display: 'none' }} />
              </div>
              <div role="button" tabIndex="0" onClick={onOpenGif}>
                <GifBoxOutlinedIcon className={styles['media-icon']} />
              </div>
            </div>
            <button type="submit" className={styles['tweet-icons-button']}>whisp</button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TweetBox;
