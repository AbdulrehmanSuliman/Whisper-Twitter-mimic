import React from 'react';
import 'react-responsive-carousel/lib/styles/carousel.min.css'; // requires a loader
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import FlashOnRoundedIcon from '@mui/icons-material/FlashOnRounded';
import FavoriteRoundedIcon from '@mui/icons-material/FavoriteRounded';
import PersonRoundedIcon from '@mui/icons-material/PersonRounded';
import TwitterIcon from '@mui/icons-material/Twitter';
import RepeatRoundedIcon from '@mui/icons-material/RepeatRounded';
import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import PropTypes from 'prop-types';
import styles from './NotiContent.module.css';
import { Route, Link, BrowserRouter, withRouter } from "react-router-dom";
import { useNavigate } from "react-router-dom";


/**
 * @param {Number} id      Id
 * @param {Number} post_id
 * @param {Number} profile_id
 * @param {String} displayname      User display name (user first name).
 * @param {String} content       text.
 * @param {String} notitype     different notifications icons.
 * @param {String} date  
 /**
 return notifications content inside feed insidd notifications component
 */

function NotiContent({
  id, post_id, profile_id, displayname, content, notitype, date,
}) {
  let navigate = useNavigate();
  let icon = null;
  let statement1 = null;
  let statement2 = null;
  let statement3 = null;
  // console.log(content);
  if (notitype === 'like') {
    icon = <FavoriteRoundedIcon className={styles['like-icon']} />;
    statement2 = ' liked your Tweet';
  } else if (notitype === 'retweet') {
    icon = <RepeatRoundedIcon className={styles['retweet-icon']} />;
    statement2 = ' Retweeted your Tweet';
  } else if (notitype === 'missed') {
    icon = <AutoAwesomeIcon className={styles['missed-icon']} />;
    statement1 = 'In case you missed ';
    statement2 = '\'s tweet'
  } else if (notitype === 'followed') {
    icon = <PersonRoundedIcon className={styles['followed-icon']} />;
    statement2 = ' followed you';
  } else if (notitype === 'login') {
    icon = <TwitterIcon className={styles['login-icon']} />;
    statement1 = 'There was a login to your account @';
    statement2 = ' from a new device on'
    statement3 = '. Review it now.'
  } else if (notitype === 'news') {
    icon = <FlashOnRoundedIcon className={styles['news-icon']} />;
    // statement = ' Liked your Tweet';
  } else {
    icon = null;
  }

  const handleOpenNoti = (e) => {
    console.log(post_id)
    console.log(profile_id)
    return navigate("/ViewTweet",{
      state: {
        post_id: post_id,
      }
     });
    // props.history.push("/ViewTweet");
    // history.push('/ViewTweet')
    // return  (<Redirect to='/Home'  />);
    setShareEl(e.currentTarget);
  };


  let pp = <AccountCircleIcon />;
  if (notitype === 'login' || notitype === 'news') {
    console.log('pppppppppp');
    if (notitype === 'news') {
      statement1 = content
    }
    pp = null;
    return (
      <button className={styles.wrapper} onClick={handleOpenNoti}>
        <div className={styles.wrapper2}>
          <div data-testid="notitype-render-test">
            {icon}
          </div>
          {/* <AccountCircleIcon /> */}
          <div className={styles['login-news']}>
            {statement1} <b>{displayname}</b> {statement2} <br></br>{date} {statement3}
          </div>
        </div>

        {' '}
        <div data-testid="content-render-test">
          <br></br>
        </div>
      </button>
    );
  }
  console.log(id);
  console.log(styles);
  return (
    <button className={styles.wrapper} onClick={handleOpenNoti}>
      <div className={styles.wrapper2}>
        <div data-testid="notitype-render-test">
          {icon}
        </div>
        {/* <AccountCircleIcon /> */}
        <div data-testid="noticontent-avatar-render-test" className={styles.postavatar}>
          {pp}
        </div>
      </div>
      <div className={styles['display-name']}>
        {statement1} <b>{displayname}</b> {statement2}
      </div>
      {' '}
      <div data-testid="content-render-test">
        <br></br>
        <div className={styles.content2}>
          {content}
        </div>
      </div>
    </button>
  );
}

NotiContent.propTypes = {
  id: PropTypes.number.isRequired,
  post_id: PropTypes.number.isRequired,
  profile_id: PropTypes.number.isRequired,
  displayname: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  notitype: PropTypes.string.isRequired,
  date: PropTypes.string.isRequired,
};

export default NotiContent;
