import kue, { createQueue } from 'kue';

const queue = createQueue();

export default function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${ phoneNumber }, `
              + `with message: ${ message }`);

}
