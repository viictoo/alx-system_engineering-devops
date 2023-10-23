#!/usr/bin/node
// api module to get data and save in json file

const https = require("https")
const process = require("process")
const fs = require("fs")

function getName() {
    const id = process.argv[2];
    console.log(id);
    const userUrl = `https://jsonplaceholder.typicode.com/users/${id}`
    const todoUrl = `https://jsonplaceholder.typicode.com/todos?userId=${id}`

    https.get(userUrl, (userResponse) => {
        let userData = '';

        userResponse.on('data', (chunk) => {
            userData += chunk;
        });
        userResponse.on('end', () => {
            const employee = JSON.parse(userData);
            const name = employee.username
            https.get(todoUrl, (todoResponse) => {
                let todoData = '';
                todoResponse.on('data', (todoChunk) => {
                    todoData += todoChunk;
                });
                todoResponse.on('end', () => {
                    const todo = JSON.parse(todoData)

                    const tasks = []
                    const jdata = {}
                    for (const task of todo) {
                        dic = {
                            "task": task.title,
                            "completed": task.completed,
                            "username": name}
                        tasks.push(dic)
                    }
                    jdata[parseInt(id)] = tasks
                    const filename  = `${id}.json`;

                    fs.writeFile(filename, JSON.stringify(jdata, null,1), (err) => {
                        if (err) throw err;
                        else {console.log(`data saved to ${filename}`);}
                    });
                });

            });
        });
    });
}
if (require.main == module) {
    getName();
}
