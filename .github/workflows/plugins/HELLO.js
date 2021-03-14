client.on('message', message => {
	if (message.content === 'hello') {
		message.channel.send('hello!');
	}
});

// now fuck off with stealing code, deffo didn't take 1 second to make :(!!
