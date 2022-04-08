// ignore_for_file: file_names

import 'package:google_sign_in/google_sign_in.dart';

class GoogleSignInApi {
  static final _googleSignIn = GoogleSignIn();
  static Future<GoogleSignInAccount?> login() => _googleSignIn.signIn();
}

// to get Sh1 in terminal or cmd
// keytool -list -v -keystore c:/Users/ET/.android/debug.keystore -alias androiddebugkey -storepass android -keypass android
