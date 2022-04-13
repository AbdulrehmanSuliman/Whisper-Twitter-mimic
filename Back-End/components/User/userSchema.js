const mongoose=require('mongoose');
const jwt = require('jsonwebtoken');
require('dotenv').config({ path: 'config.env'});

const userSchema = new mongoose.Schema ({

    name: {type :String ,required :true,trim: true},
    username: { type :String ,trim: true, unique: true},
    email: { type :String ,required :true,trim: true, unique: true},
    password: { type: String},
    googleId:{ type:String},
    facebookId:{ type:String},
    passwordResetOTP:{type:String,minlength: 8,maxlength: 1024},
    role:{ type:String ,enum: ['User' , 'Admin'],default:'User',trim: true},
    profilePic: {type: String}, // TODO:add default picture url
    coverPhoto: {type: String},
    birthdate:{type: Date},
    description: {type: String},
    //location	
    //private: { type:Boolean ,default: false}, //whether account is private or public
    followers: [ { type: mongoose.Schema.Types.ObjectId, ref:'User'} ],
    following: [ { type: mongoose.Schema.Types.ObjectId, ref:'User'} ],
    blocks: [ { type: mongoose.Schema.Types.ObjectId, ref:'User'} ],
    likes: [ {type: mongoose.Schema.Types.ObjectId ,ref: 'Tweet' }],
    bookmarks: [ {type: mongoose.Schema.Types.ObjectId ,ref: 'Tweet' }]
    //TODO : add list of tweets (refrences tweet schema)
    //add pinned tweets (refrences tweet schema)	
    // banned boolean
    // ban startDate and endDate
    // banning adminID   
},{timestamps: true});

userSchema.methods.generateJWT = function (){
    const token = jwt.sign({
        _id: this._id,
        email: this.email,
        role: this.role
    },process.env.JWT_SECRET_KEY ,{expiresIn :'1d'});
    return token;
}
const User= mongoose.model('User',userSchema);
module.exports = User;
