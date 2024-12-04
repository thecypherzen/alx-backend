import { createClient } from 'redis';

/* eslint-disable */
const client = createClient()
      .on('error', (err) => {
        console.log(
          `Redis client not connected to the server: ${err.message}`);
      }).connect()
      .then(() => {
        console.log('Redis client connected to the server');
      });


export { client };
