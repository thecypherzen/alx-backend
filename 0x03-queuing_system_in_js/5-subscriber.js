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

client.subscribe('holberton school channel',
                 (msg) => console.log(msg))
      .then((res) => {
        if (res) {
          console.log(res);
        }
      })
      .catch(err => console.log(err));
