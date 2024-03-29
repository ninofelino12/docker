// File generated by FlutterFire CLI.
// ignore_for_file: lines_longer_than_80_chars, avoid_classes_with_only_static_members
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for windows - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      case TargetPlatform.linux:
        return macos;
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyAOlqz2Eaf7s5CWgjp8IlESvLBIyhC-sGM',
    appId: '1:856774459322:web:7efec70566cdc65af5e783',
    messagingSenderId: '856774459322',
    projectId: 'odoodb-afb24',
    authDomain: 'odoodb-afb24.firebaseapp.com',
    databaseURL: 'https://odoodb-afb24-default-rtdb.firebaseio.com',
    storageBucket: 'odoodb-afb24.appspot.com',
    measurementId: 'G-T97HT0CNVW',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyBARDg5zparzMVMmn5wmXKf-M9ZR36Ejms',
    appId: '1:856774459322:android:e2af9dc0e15505b9f5e783',
    messagingSenderId: '856774459322',
    projectId: 'odoodb-afb24',
    databaseURL: 'https://odoodb-afb24-default-rtdb.firebaseio.com',
    storageBucket: 'odoodb-afb24.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyCXutwHyB_zouaxRQuUn4Gh672gADtUsQQ',
    appId: '1:856774459322:ios:6bc8082e9cc52b98f5e783',
    messagingSenderId: '856774459322',
    projectId: 'odoodb-afb24',
    databaseURL: 'https://odoodb-afb24-default-rtdb.firebaseio.com',
    storageBucket: 'odoodb-afb24.appspot.com',
    iosBundleId: 'com.example.firebase',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyCXutwHyB_zouaxRQuUn4Gh672gADtUsQQ',
    appId: '1:856774459322:ios:39003ea3bc06ddfff5e783',
    messagingSenderId: '856774459322',
    projectId: 'odoodb-afb24',
    databaseURL: 'https://odoodb-afb24-default-rtdb.firebaseio.com',
    storageBucket: 'odoodb-afb24.appspot.com',
    iosBundleId: 'com.example.firebase.RunnerTests',
  );

  static const FirebaseOptions linux = FirebaseOptions(
    apiKey: 'AIzaSyCXutwHyB_zouaxRQuUn4Gh672gADtUsQQ',
    appId: '1:856774459322:ios:39003ea3bc06ddfff5e783',
    messagingSenderId: '856774459322',
    projectId: 'odoodb-afb24',
    databaseURL: 'https://odoodb-afb24-default-rtdb.firebaseio.com',
    storageBucket: 'odoodb-afb24.appspot.com',
    iosBundleId: 'com.example.firebase.RunnerTests',
  );
}
