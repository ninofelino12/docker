import 'package:appfluter/photo.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

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

class MyHomePage extends StatelessWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: Text(title, style: TextStyle(color: Colors.white)),
        actions: [
          IconButton(
              icon: Icon(Icons.search),
              onPressed: () {
                // Add search code here
              }),
          IconButton(
              icon: Icon(Icons.add),
              onPressed: () {
                // Add widget code here
              }),
          IconButton(
            icon: Icon(Icons.camera),
            onPressed: () {
              // Add camera button code here
            },
          )
        ],
      ),
      body: FutureBuilder<List<Photo>>(
        future: fetchPhotos(http.Client()),
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
                Text(photos[index].title,
                    style: const TextStyle(backgroundColor: Colors.red)),
                Text(photos[index].name,
                    style: TextStyle(backgroundColor: Colors.red)),
                Text(photos[index].url,
                    style: TextStyle(backgroundColor: Colors.red))
              ],
            ),
          ],
        );
      },
    );
  }
}

class coli extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      child: Text('This is a stateless widget'),
    );
  }
}
