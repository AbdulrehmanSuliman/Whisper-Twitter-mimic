import React from 'react';
import PropTypes from 'prop-types';
import styles from './NotiFeed.module.css';
import NotiContent from './NotiContent';
/**
 * @param {array} data array containing our notifications.
 * @returns map through the post array data and starts passing the notifications props
 * to display the notifications in the feed component.
 */
function NotiFeed({ data }) {
  return (
    <div data-testid="notifeed-render-test" className={styles.notifeed}>

      <div data-testid="noticontent-render-test" className={styles.parent}>

        {
        data && data.map((content) => (
          // <section className={styles.feedbox1}>
          //   <button className={styles.feedbox2} type="button">
          <NotiContent
            id={content.id}
            postid={content.postid}
            profileid={content.profileid}
            displayname={content.displayname}
            content={content.content}
            notitype={content.notitype}
            date={content.date}
          />
          //   </button>
          // </section>
        ))
    }
        <div className={styles.emptyspace} />
      </div>
    </div>

  );
}
NotiFeed.propTypes = {
  data: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.number.isRequired,
    displayname: PropTypes.string.isRequired,
    content: PropTypes.string.isRequired,

    notitype: PropTypes.string.isRequired,
  })).isRequired,
};
export default NotiFeed;
