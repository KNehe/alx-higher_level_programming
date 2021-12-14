#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const el of list) {
    if (el === searchElement) count++;
  }
  return count;
};
