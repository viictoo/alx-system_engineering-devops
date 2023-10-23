const https = require('https');
const process = require('process');

function getData() {
    const id = process.argv[2];
    const todoUrl = `https://jsonplaceholder.typicode.com/todos?userId=${id}`;
    const userUrl = `https://jsonplaceholder.typicode.com/users/${id}`;

    https.get(todoUrl, (todoResponse) => {
        let todoData = '';

        todoResponse.on('data', (chunk) => {
            todoData += chunk;
        });

        todoResponse.on('end', () => {
            const resp = JSON.parse(todoData);

            https.get(userUrl, (userResponse) => {
                let userData = '';

                userResponse.on('data', (userChunk) => {
                    userData += userChunk;
                });

                userResponse.on('end', () => {
                    const employee = JSON.parse(userData);
                    const name = employee.name;

                    const tasks = [];
                    let total = 0;
                    let completed = 0;

                    for (const task of resp) {
                        total += 1;
                        if (task.completed === true) {
                            tasks.push(task.title);
                            completed += 1;
                        }
                    }

                    console.log(`Employee ${name} is done with tasks(${completed}/${total}):`);
                    for (const tsk of tasks) {
                        console.log(`\t${tsk}`);
                    }
                });
            });
        });
    });
}

if (require.main === module) {
    getData();
}
