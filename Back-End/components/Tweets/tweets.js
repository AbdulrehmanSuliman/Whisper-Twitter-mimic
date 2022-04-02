const express = require('express');
const router = express.Router();
const bodyParser = require('body-parser');
const user = require('../User/userSchema');
const tweet=require('./tweetsSchema'); //returns the model 

// const { redirect } = require("express/lib/response");
// const express = require('express');
// const app=express();
// app.use(bodyParser.urlencoded({extended: false}));


const multer=require('multer')

const filestorageEngine=multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null,"./uploads")
    },
    filename:(req,file,cb) => {
    cb (null,Date.now()+"-"+file.originalname);
    }
});

objectMulter={
    storage: filestorageEngine
}

const upload=multer(objectMulter).array('im',4);



// const u1=new user({
//     name:"AliAdel",
//     username: "Ali_adell098",
//     email: "ali2000@gmail.com",
//     password: "123"
// });
// u1.save();

// const t1=new tweet({
//     content:"hi world"
// })
// t1.save()


router.post("/", function(req,res){

    upload(req,res,function(err){
    if(err){
            console.log("here")
            res.sendStatus(400);
            
        }
    
    else
    {console.log("awel 7aga")

    let token = req.headers["authorization"]
    token = token.split(" ")[1];
    console.log(token)
    // token="623ed35374a406aca722ac9b"

        mediaTemp=[]
     contentTemp=""
     console.log("iam here");
        
     
     if(req.body.tweetContent!=""){
        console.log("the tweet:"+ req.body.tweetContent)
         contentTemp=req.body.tweetContent
     }
 
 
     if(!req.files){
         console.log("no img")
     }
     else{
         m=req.files
         for(i=0;i<m.length;i++)
          {
                 mediaTemp.push(req.files[i].path)
          }
     }
 
     if(contentTemp!="" || mediaTemp!="")
     {
            
            const userTweet= new tweet({
             content: req.body.tweetContent,
             postedBy: token,
             likes: token,
             retweeters:  token,
             retweetInfo:  token,
             media: mediaTemp
         });
 
             userTweet.save(async function(err){
             if(err)
             {
                 console.log("heeree");
                 res.sendStatus(400);
             }
             else
             {
                 await user.populate(userTweet, { path: "postedBy" });
                 await user.populate(userTweet, { path: "likes" });
                 await user.populate(userTweet, { path: "retweeters" });
                 await tweet.populate(userTweet, { path: "retweetInfo" });
                 res.sendStatus(200);
             }
         });
     }
     else{
         console.log("hiooooo")
         res.sendStatus(400);
     }
    }
 });
});
 
 
 //Deleting a tweet:
 router.delete("/:id", function(req, res){
     tweet.findByIdAndDelete(req.params.id)
     .then(() => res.sendStatus(202))
     .catch(function(error){
            res.sendStatus(400);
     })
 })

//  router.get("/LikesCount/:id",function(req,res){
//      tweetTuple=tweet.findById(req.params.id)
     
//      .then(() => res.sendStatus(202))
//      .catch(function(error){
//             res.sendStatus(400);
//      })

//  })



module.exports =router;
