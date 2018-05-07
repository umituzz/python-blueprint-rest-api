class Item:
    id=""
    title = ""
    description = ""
    def __init__(self,id,title,description):
        self.id = id
        self.title = title
        self.description = description
    def toJson(self):
        in_json = {"id":self.id,"title":self.title,"description":self.description}
        return in_json
    def toJson2(self):
        return self.__dict__

todoList = []
item1 = Item(id="1",title="Merhaba Dünya",description="Hello World in different languages")
item2 = Item(id="2",title="Olağan Dünya",description="Herkes kendi kafasını yaşıyor")

todoList.append(item1.toJson())
todoList.append(item2.toJson2())