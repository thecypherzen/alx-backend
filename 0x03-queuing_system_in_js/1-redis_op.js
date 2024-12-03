import redis, { createClient } from 'redis';


const client = await createClient()
    .on('error', (err) => {
      console.log(
        `Redis client not connected to the server: ${err.message}`
      );
    })

await client.connect();
console.log("connection established");
if (client.isReady) {
  console.log('Redis client connected to the server');
}


function setNewSchool(schoolName, value) {
  client.set(schoolName, value)
        .then(res => console.log(`Reply: ${res}`))
        .catch(err => console.log(err.message));
}

function displaySchoolValue(schoolName) {
  client.get(schoolName)
        .then(res => console.log(res))
        .catch(err => console.log(err.message));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
