// ignore_for_file: unused_import

import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:whisper/layout/Admin/GraphPie.dart';
import 'package:whisper/layout/WelcomePage.dart';
import 'package:whisper/layout/UserProfile/profile_layout.dart';
import 'package:whisper/layout/Admin/AdminPage.dart';
import 'package:whisper/models/date_time_format.dart';

import 'layout/Timeline/Timeline.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(
    const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: //WelcomePage(),
          //ProfilePage(),
          AdminPage(),
      //TimelinePage(), //need to remove const from MaterialApp in line 17
    ),
  );
}
