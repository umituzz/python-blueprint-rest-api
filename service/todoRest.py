from flask import Flask, request, Response, jsonify,Blueprint
from model import Item,todoList
blueprint = Blueprint('todo',__name__,url_prefix="/todo")





@blueprint.route("/list",methods=["GET"])
def getAllTodos():
    return jsonify(todoList)
@blueprint.route("/",methods=["POST"])
def createNewTodoItem():
    item = Item(**request.get_json())
    todoList.append(item.toJson())
    return Response('{"message":"success"}',status=201,mimetype='application/json')
@blueprint.route("/<id>")
def findTodoItemById(id):
    itemToReturn = None
    for item in todoList:
        if item["id"] == id:
            itemToReturn = item
        else:
            continue
    if itemToReturn == None:
        return Response('{"message":"item not found"}', status=404, mimetype='application/json')
    else:
        response = jsonify(itemToReturn)
        response.status_code = 200
        return response
@blueprint.route("/", methods=["PUT"])
def updateExistingTodoItem():
    item = Item(**request.get_json())
    isExist = False
    for i in todoList:
        if i["id"] == item.id:
            i["title"] = item.title
            i["description"] = item.description
            isExist = True
            break
    if isExist:
        response = jsonify({"message":"Item updated successfully"})
        response.status_code = 201
        return response
    else:
        response = jsonify({"message":"Item not exist"})
        response.status_code = 404
        return response

@blueprint.route("/<id>", methods=["DELETE"])
def deleteTodoItemById(id):
    itemToDelete = None
    for item in todoList:
        if item["id"] == id:
            itemToDelete = item
        else:
            continue
    if itemToDelete == None:
        response = jsonify({"message": "Item not found"})
        response.status_code = 404
        return response
    else:
        todoList.remove(itemToDelete)
        response = jsonify({"message": "Item removed successfully"})
        response.status_code = 201
        return response

