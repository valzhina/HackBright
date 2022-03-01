'use strict';

// 1. printIndices
function printIndices(items) {
  //Print each item in the list, followed by its index.//
  for (const i in items) {
    // console.log(i);
     console.log(`${items[i]} ${i}`);
  }
}

// 2. everyOtherItem
function everyOtherItem(items) {
  const result = [];

  for (const i in items) {
    if (i % 2 === 0) {
      result.push(items[i]);
    }
  }
  console.log(result);
}

// 3. smallestNItems
function smallestNItems(items, n) {
  const sorItems = items.sort((a, b) => a - b) //; not to use here
  sorItems.slice(0, n);
  sorItems.reverse();

  console.log(sorItems);
}
