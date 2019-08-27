from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt
import json


def initialize_project():

    style = style_from_dict({
        Token.QuestionMark: '#E91E63 bold',
        Token.Selected: '#673AB7 bold',
        Token.Instruction: '',  # default
        Token.Answer: '#2196f3 bold',
        Token.Question: '',
    })

    questions = [
        {
            'type': 'input',
            'name': 'name',
            'message': 'Package name:',
            'default': 'qwe'
        },
        {
            'type': 'input',
            'name': 'version',
            'message': 'Version:',
            'default': '1.0.0',
        },
        {
            'type': 'input',
            'name': 'description',
            'message': 'Description:',
            'default': '',
        },
        {
            'type': 'input',
            'name': 'repository',
            'message': 'Repository:',
        },
        {
            'type': 'input',
            'name': 'author',
            'message': 'Author:',
        },
        {
            'type': 'input',
            'name': 'keywords',
            'message': 'Keywords:',
        },
        {
            'type': 'input',
            'name': 'license',
            'message': 'License:',
        },

    ]
    answers = prompt(questions, style=style)
    if answers:
        with open('app.json', 'w') as config:
            json.dump(answers, config, indent=4)
