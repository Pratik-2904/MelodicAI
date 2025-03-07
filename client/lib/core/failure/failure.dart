// ignore_for_file: public_member_api_docs, sort_constructors_first
class Failure {
  final String message;
  final String? statusCode;
  Failure([this.message = "Something went wrong", this.statusCode]);

  @override
  String toString() => 'Failure(message: $message, statusCode: $statusCode)';
}
