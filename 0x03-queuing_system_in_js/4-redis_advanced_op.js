import { createClient } from 'redis';


const client = await createClient()
    .on('error', (err) => {
      console.log(
        `Redis client not connected to the server: ${err.message}`
      );
    })

await client.connect();
if (client.isReady) {
  console.log('Redis client connected to the server');
}
client.del('HolbertonSchools');
client.hSet('HolbertonSchools', 'Portland', 50)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message));
client.hSet('HolbertonSchools', 'Seattle', 80)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message));
client.hSet('HolbertonSchools', 'New York', 20)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message));
client.hSet('HolbertonSchools', 'Bogota', 20)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message));
client.hSet('HolbertonSchools', 'Cali', 40)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message));
client.hSet('HolbertonSchools', 'Paris', 2)
      .then((res) => console.log(res))
      .catch((err) => console.log(err.message));

client.hGetAll('HolbertonSchools')
      .then((val) => console.log({...val}));
