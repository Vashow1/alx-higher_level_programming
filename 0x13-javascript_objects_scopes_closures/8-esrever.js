#!/usr/bin/node

exports.esrever = function (list) {
	let i = list.length - 1;
	let j = 0;
	let reversed = []
	for (i, j; list[i]; i--, j++) {
		reversed[j] = list[i];
	}
	return (reversed);
}
