import 'package:appfluter/photo.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

String myUrl = 'http://localhost:8015/gateway/product';
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    const appTitle = 'Isolate Demo';

    return const MaterialApp(
      title: appTitle,
      home: MyHomePage(title: appTitle),
    );
  }
}

Future<List<Photo>> fetchPhotos2(http.Client client, String example) async {
  // final response = await client.get(Uri.parse(myUrl));
  final response = await client.get(Uri.parse(example));
  return compute(parsePhotos, response.body);
}

class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: Text(title, style: const TextStyle(color: Colors.white)),
        actions: [
          IconButton(
              icon: const Icon(Icons.search),
              onPressed: () {
                myUrl = 'http://localhost:8r015/gateway/product//';

                print(myUrl);
                // Add search code here
              }),
          IconButton(
              icon: const Icon(Icons.add),
              onPressed: () {
                // Add widget code here
              }),
          IconButton(
            icon: const Icon(Icons.camera),
            onPressed: () {
              // Add camera button code here
            },
          )
        ],
      ),
      body: FutureBuilder<List<Photo>>(
        future: fetchPhotos2(http.Client(), myUrl),
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return const Center(
              child: Text('An error has occurred!'),
            );
          } else if (snapshot.hasData) {
            return PhotosList(photos: snapshot.data!);
          } else {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }
        },
      ),
    );
  }
}

class PhotosList extends StatelessWidget {
  const PhotosList({super.key, required this.photos});

  final List<Photo> photos;

  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 4,
      ),
      itemCount: photos.length,
      itemBuilder: (context, index) {
        // return Image.network(photos[index].thumbnailUrl);
        //
        return Column(
          children: [
            Column(
              children: [
                Text(photos[index].title),
                Text(photos[index].name),
                Text(myUrl),
                Text(photos[index].url)
              ],
            ),
            // Image.network(photos[index].thumbnailUrl), // Added image widget
            Image.network('http://localhost:8015/gateway/png?id=' +
                photos[index].id.toString())
          ],
        );
      },
    );
  }
}
