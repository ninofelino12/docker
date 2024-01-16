import 'package:firebase_database/firebase_database.dart';
import 'package:firedart/firedart.dart';

const apiKey = 'AIzaSyCXutwHyB_zouaxRQuUn4Gh672gADtUsQQ';
const projectId = 'odoodb-afb24';
const email = 'ninofelino12@gmail.com';
const password = '1234578';

Future main() async {
  FirebaseAuth.initialize(apiKey, VolatileStore());
  Firestore.initialize(projectId); // Firestore reuses the auth client
  FirebaseDatabase database = FirebaseDatabase.instance;
  DatabaseReference ref = FirebaseDatabase.instance.ref("users/123");

  await ref.set({
    "name": "John",
    "age": 18,
    "address": {"line1": "100 Mountain View"}
  });
}
