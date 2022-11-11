from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.recipe import Recipe

@app.route('/recipe/new')
def new_recipe():
    return render_template("new_recipe.html")

@app.route('/recipe/create',methods=['POST'])
def create_recipe():
    print(request.form)
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("recipes.html",recipes=Recipe.get_all_with_users())

@app.route('/recipe/show/<int:id>')
def show_recipes(id):
    data ={ 
        "id":id
    }
    return render_template("show_recipe.html",recipe=Recipe.get_one(data))

@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    data ={ 
        "id":id
    }
    return render_template("edit_recipe.html",recipe=Recipe.get_one(data))

@app.route('/recipe/update',methods=['POST'])
def update_recipe():
    Recipe.update(request.form)
    return redirect('/recipes')

@app.route('/recipe/destroy/<int:id>')
def destroy_recipe(id):
    data ={
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/recipes')