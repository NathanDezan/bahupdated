import json
# from src.integration.notion.Properties import Properties

class Schema:
    def __init__(self):
        self.schema = self.create()

    def create(self):
        try:
            with open('schema.json') as f:
                schema = json.load(f)
            return schema
        except Exception as e:
            return None
    
    def set_database_id(self, database_id):
        try:
            self.schema['parent']['database_id'] = database_id
            return self.schema
        except Exception as e:
            return None
    
    def set_icon(self, emoji):
        try:
            self.schema['icon']['emoji'] = emoji
            return self.schema
        except Exception as e:
            return None
    
    def set_cover(self, url):
        try:
            self.schema['cover']['external']['url'] = url
            return self.schema
        except Exception as e:
            return None
    
    def set_title(self, title):
        try:
            self.schema['properties']['Title']['title'][0]['text']['content'] = title
            return self.schema
        except Exception as e:
            return None
    
    def set_category(self, list_categories, color):
        try:
            list_category = []
            for category in list_categories:
                temp_category = {
                    "name": category,
                    "color": color
                }
                list_category.append(temp_category)
            self.schema['properties']['Category']['multi_select'] = list_category
            return self.schema
        except Exception as e:
            return None
    # def set_title(self, title):
    #     try:
    #         self.schema['properties']['Title']['title'][0]['text']['content'] = title
    #         return self.schema
    #     except Exception as e:
    #         return None

temp_schema = Schema()
json_schema = temp_schema.schema

for i in json_schema:
    # print(i, json_schema[i])
    print(i)