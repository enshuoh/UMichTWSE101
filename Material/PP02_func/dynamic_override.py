import types
class a:
  def whoami(self):
      print("I am a")

b = a()
b.whoami()

def new_whoami(self):
    print("I am b")

b.whoami = types.MethodType(new_whoami, b)
