import kue, { createQueue } from 'kue';

const push_notification_code = createQueue();

let job = push_notification_code.create(
  { phoneNumber: '233232',
    message: 'notification message',
  }
).save((err) => {
  if (err) {
    console.log('Notification job failed');
  } else {
    console.log(`Notification job created: ${job.id}`);
  }
});
// handle error
push_notification_code.on(
  'error', (err) => {console.log('error:', err.message)});
push_notification_code.on('job complete', (err, job) => {
  if (err) return;
  console.log('Notification job completed');
  job.remove((err) => {
    if (err) console.log(err.message);
  })
})
