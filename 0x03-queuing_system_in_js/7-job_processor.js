// import push_notification_code_2 from './7-job_creator.js';
import { createQueue } from 'kue';

const queue = createQueue();
const blockedNumbers = ['4153518780', '4153518781'];
function sendNotification(phoneNumber, message,
                         job, done) {
  if (blockedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${ phoneNumber } `
                          +`is blacklisted`));
  } else {
    let total = 100,
        stepsLeft = 100;
    let interval = setInterval(() => {
      job.progress(total - stepsLeft, total);
      console.log(`Sending notification to ${ phoneNumber },`
                  + ` with message: ${ message }`);
      stepsLeft -= 50;
      stepsLeft || done();
      stepsLeft || clearInterval(interval);
    }, 1000);
  }
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message,
  job, done);
});
