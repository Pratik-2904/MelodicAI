import 'package:client/core/model/usermodel.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';

part 'current_user_notifier.g.dart';

@Riverpod(keepAlive: true)
class CurrentUserNotifier extends _$CurrentUserNotifier {
  @override
  Usermodel? build() {
    return null;
  }

  void addUser(Usermodel usermodel) {
    state = usermodel;
  }
  void removeUser() {
    state = null;
  }
}
