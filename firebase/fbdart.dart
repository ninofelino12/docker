import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';

void main() async {
  // Buat instance FirebaseApp
  await FirebaseApp.initializeApp();

  // Buat instance DatabaseReference
  final database = FirebaseDatabase.instance.ref();

  // Tulis data ke database
  database.child('data').set({'key': 'value'});

  // Baca data dari database
  final data = await database.child('data').get();
  print(data); // {key: value}
}
