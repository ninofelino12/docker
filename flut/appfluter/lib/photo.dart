import 'dart:convert';

class Photo {
  final int albumId;
  final int id;
  final String title;
  final String url;
  final String thumbnailUrl;
  final String name;

  const Photo({
    required this.albumId,
    required this.id,
    required this.title,
    required this.url,
    required this.thumbnailUrl,
    required this.name,
  });

  factory Photo.fromJson(Map<String, dynamic> json) {
    return Photo(
      albumId: json['id'] as int,
      id: json['id'] as int,
      title: json['name'] as String,
      url: json['dd'] as String,
      thumbnailUrl: json['name'] as String,
      name: json['name'] as String,
    );
  }
}

List<Photo> parsePhotos(String responseBody) {
  final parsed =
      (jsonDecode(responseBody) as List).cast<Map<String, dynamic>>();

  return parsed.map<Photo>((json) => Photo.fromJson(json)).toList();
}
