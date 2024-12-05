import { createQueue } from 'kue';

const queue = createQueue();
const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account'
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account'
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account'
  }
];

jobs.forEach((task) => {
  let job = queue
      .create('push_notification_code_2', task)
      .save((err) => {
        if (err) {
          console.log(err);
        } else {
          console.log(`Notification job created: ${job.id}`);
        }
      })
});
queue
  .on('job complete', (id) => {
    console.log(`Notification job ${id} completed`)
  })
  .on('job failed', (id, msg) => {
    console.log(`Notification job ${id} failed: ${msg}`)
  })
  .on('job progress', (id, level) => {
    console.log(`Notification job ${ id } ${ level }% complete`)
  });