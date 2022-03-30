import 'package:flutter/material.dart';
import 'package:twitter_app/login.dart';
//import 'package:twitter_app/login.dart';
//import 'package:google_sign_in/google_sign_in.dart';
import 'package:sign_button/sign_button.dart';
import 'package:twitter_app/API/google_signIn_api.dart';
//import 'package:flutter_signin_button/flutter_signin_button.dart';

class SignUpPage extends StatelessWidget {
  const SignUpPage({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      resizeToAvoidBottomInset: true,
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 5,
        backgroundColor: Colors.white,
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: const Icon(
            Icons.arrow_back_ios,
            size: 20,
            color: Colors.black,
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.symmetric(horizontal: 40),
          height: MediaQuery.of(context).size.height - 50,
          width: double.infinity,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            children: <Widget>[
              Column(
                children: <Widget>[
                  const Text(
                    "Sign Up",
                    style: TextStyle(
                      fontSize: 30,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(
                    height: 20,
                  ),
                  Text(
                    "Create an Account",
                    style: TextStyle(fontSize: 15, color: Colors.grey[700]),
                  )
                ],
              ),
              Column(
                children: <Widget>[
                  inputFile(label: "Username"),
                  inputFile(label: "Email"),
                  inputFile(label: "Password", obscureText: true),
                  inputFile(label: "Confirm Password", obscureText: true),
                ],
              ),
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 0),
                decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(50),
                    border: const Border(
                      bottom: BorderSide(color: Colors.black),
                      top: BorderSide(color: Colors.black),
                      left: BorderSide(color: Colors.black),
                      right: BorderSide(color: Colors.black),
                    )),
                child: MaterialButton(
                  minWidth: double.infinity,
                  height: 60,
                  onPressed: () {},
                  color: const Color(0xff0095FF),
                  elevation: 5,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(50),
                  ),
                  child: const Text(
                    "Sign Up",
                    style: TextStyle(
                      fontWeight: FontWeight.w600,
                      fontSize: 18,
                      color: Colors.white,
                    ),
                  ),
                ),
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  Expanded(
                    child: MaterialButton(
                      minWidth: double.infinity,
                      height: 20,
                      onPressed: () {
                        Navigator.push(
                            context,
                            MaterialPageRoute(
                                builder: (context) => const LoginPage()));
                      },
                      child: const Text(
                        "Already have an account? Log in",
                        style: TextStyle(
                          fontWeight: FontWeight.w400,
                          fontSize: 14,
                          color: Color.fromARGB(255, 0, 0, 0),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              Row(
                children: <Widget>[
                  Expanded(
                    child: SignInButton.mini(
                        buttonType: ButtonType.facebook,
                        onPressed: signIn2 //() => null,
                        ),
                  ),
                  Expanded(
                    child: SignInButton.mini(
                        buttonType: ButtonType.google,
                        onPressed: signIn //() => null,
                        ),
                  )
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  Future signIn() async {
    await GoogleSignInApi.login();
  }

  Future signIn2() async {
    await GoogleSignInApi.login();
  }
}
