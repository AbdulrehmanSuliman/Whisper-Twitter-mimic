// ignore_for_file: file_names, avoid_unnecessary_containers, non_constant_identifier_names, unnecessary_new, avoid_print, avoid_init_to_null, unused_local_variable, duplicate_import, prefer_typing_uninitialized_variables, camel_case_types

// import 'dart:io';

import 'package:flutter/material.dart';
import 'package:whisper/layout/Admin/GraphBar.dart';
import 'package:whisper/layout/Admin/GraphPie.dart';
import 'package:whisper/modules/AdminTweetBoxWidget.dart';
import 'package:whisper/models/tweet_model.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class AdminPage extends StatefulWidget {
  final String token;
  const AdminPage({Key? key, required this.token}) : super(key: key);
  @override
  _AdminPage createState() => _AdminPage();
}

class _AdminPage extends State<AdminPage> {
  @override
  initState() {
    //NoUsers(widget.token);
    //NoBanned(widget.token);
    //ratioTweets(widget.token);
    super.initState();
  }

  late var NoUser = 5;
  late var NoBan = 5;
  late var ratioTweet = '';
  Future NoUsers(token) async {
    var jsonData = null;
    Map mapResponse;
    Map dataResponse;
    var response = await http.get(
      Uri.parse(
        ('http://10.0.2.2:8080/admins/statistics/noUsers'),
        //   //'http://habibsw-env-1.eba-rktzmmab.us-east-1.elasticbeanstalk.com/api/admins/statistics/noUsers'),
      ),
      headers: {
        'x-auth-token': token,
      },
    );
    setState(() {
      mapResponse = json.decode(response.body);
      dataResponse = mapResponse['noUsers'];
      NoUser = dataResponse['count'];
    });
  }

  Future NoBanned(token) async {
    Map mapResponse;
    Map dataResponse;
    var response = await http.get(
      Uri.parse(
        'http://10.0.2.2:8080/admins/statistics/noBanned',
        //'https://www.thegrowingdeveloper.org/apiview?id=1',
        //   //'http://habibsw-env-1.eba-rktzmmab.us-east-1.elasticbeanstalk.com/api/admins/statistics/noUsers'),
      ),
      headers: {'x-auth-token': token},
    );
    setState(() {
      mapResponse = json.decode(response.body);
      dataResponse = mapResponse['noBanned'];
      NoBan = dataResponse['count'];
    });
  }

  Future ratioTweets(token) async {
    Map mapResponse;
    Map dataResponse;
    var response = await http.get(
      Uri.parse(
        'http://10.0.2.2:8080/admins/statistics/ratioTweets',
        //'https://www.thegrowingdeveloper.org/apiview?id=1',
        //   //'http://habibsw-env-1.eba-rktzmmab.us-east-1.elasticbeanstalk.com/api/admins/statistics/noUsers'),
      ),
      headers: {'x-auth-token': token},
    );
    setState(() {
      mapResponse = json.decode(response.body);
      dataResponse = mapResponse['ratioTweets'];
      ratioTweet = dataResponse['count'];
    });
  }

  @override
  Widget build(BuildContext context) {
    NoUsers(widget.token);
    NoBanned(widget.token);
    ratioTweets(widget.token);
    return Scaffold(
      resizeToAvoidBottomInset: false,
      backgroundColor: Colors.white,
      body: DefaultTabController(
        length: 3,
        child: Scaffold(
          appBar: AppBar(
            bottom: const TabBar(
              tabs: [
                Text(
                  "Dashboard",
                  style: TextStyle(
                    color: Color.fromARGB(255, 255, 255, 255),
                    fontSize: 16,
                  ),
                ),
                Text(
                  "Users",
                  style: TextStyle(
                    color: Color.fromARGB(255, 255, 255, 255),
                    fontSize: 16,
                  ),
                ),
                Text(
                  "Blocked Users",
                  style: TextStyle(
                    color: Color.fromARGB(255, 255, 255, 255),
                    fontSize: 16,
                  ),
                ),
              ],
            ),
            title: const Text(
              "Admin Home",
              style: TextStyle(
                fontSize: 25,
              ),
            ),
            centerTitle: true,
          ),
          body: TabBarView(
            children: [
              Container(
                child: GridView.count(
                  crossAxisSpacing: 0,
                  mainAxisSpacing: 0,
                  crossAxisCount: 1,
                  children: [
                    Padding(
                      padding: const EdgeInsets.only(
                          left: 50, right: 50, top: 0, bottom: 50),
                      child: _AdminCard(
                        context: context,
                        count: NoUser,
                        icon: Icons.person,
                        name: " No. of Users",
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.only(
                          left: 50, right: 50, top: 0, bottom: 50),
                      child: _AdminCard(
                        context: context,
                        count: NoBan,
                        icon: Icons.block,
                        name: " No. of banned Users",
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.only(
                          left: 25, right: 50, top: 0, bottom: 50),
                      child: _AdminCard(
                        context: context,
                        count: ratioTweet,
                        icon: Icons.percent_sharp,
                        name: " Tweets Increased by",
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.only(
                          left: 50, right: 50, top: 0, bottom: 50),
                      child: Container(
                          child: Column(
                        children: <Widget>[
                          Text(
                            "Users's Age Ranges",
                            style: TextStyle(
                              fontSize: 25,
                              color: Colors.grey[700],
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(height: 25),
                          const Expanded(child: GraphPie())
                        ],
                      )),
                    ),
                    Padding(
                      padding: const EdgeInsets.only(
                          left: 50, right: 50, bottom: 100, top: 0),
                      child: Container(
                          child: Column(
                        children: <Widget>[
                          Text(
                            "Most Followed",
                            style: TextStyle(
                              fontSize: 25,
                              color: Colors.grey[700],
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                          const SizedBox(height: 25),
                          Expanded(child: GraphBar(token: widget.token))
                        ],
                      )),
                    ),
                  ],
                ),
              ),
              SingleChildScrollView(
                child: Container(
                  child: AdminTweetBoxWidget(Tweets, false, () {}),
                ),
              ),
              SingleChildScrollView(
                child: Container(
                  child: AdminTweetBoxWidget(Tweets, false, () {}),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _AdminCard(
      {required IconData icon,
      required var count,
      required String name,
      required BuildContext context}) {
    return Card(
      child: Container(
        child: Column(
          children: [
            Padding(
              padding: const EdgeInsets.only(
                  left: 12, right: 12, top: 25, bottom: 25),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(
                    icon,
                    size: 35,
                    color: Colors.blue,
                  ),
                  Text(
                    name,
                    style: const TextStyle(
                        fontSize: 25,
                        color: Colors.black,
                        fontWeight: FontWeight.bold),
                  ),
                ],
              ),
            ),
            Container(
              child: Padding(
                padding: const EdgeInsets.only(
                    left: 100, right: 0, top: 50, bottom: 25),
                child: Row(
                  children: [
                    Text(
                      count.toString(),
                      style: const TextStyle(
                          fontSize: 100, fontWeight: FontWeight.bold),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

final List<AdminTweetModel> Tweets = [
  AdminTweetModel(
    username: " Kareem",
    //tweet: "Lorem ipsum dolor sit amet",
    //time: "7h",
    twitterHandle: "@Kareem1",
  ),
  AdminTweetModel(
      username: "Ahmed",
      //tweet: "Lorem ipsum dolor sit amet",
      //time: "3m",
      twitterHandle: "@Ahmed28"),
  AdminTweetModel(
    username: " Kareem",
    //tweet: "Lorem ipsum dolor sit amet",
    //time: "7h",
    twitterHandle: "@Kareem1",
  ),
  AdminTweetModel(
      username: "Ahmed",
      //tweet: "Lorem ipsum dolor sit amet",
      //time: "3m",
      twitterHandle: "@Ahmed28"),
  AdminTweetModel(
      username: "Hassan",
      //tweet: "Lorem ipsum dolor sit amet",
      //time: "3m",
      twitterHandle: "@Hassan212"),
];
