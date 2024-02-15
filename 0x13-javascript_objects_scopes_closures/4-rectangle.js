#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
      if (w > 0 && !Number.isNaN(w) && h > 0 && !Number.isNaN(h)) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let i = 0; i < this.height; i++) {
        let result = '';
        for (let j = 0; j < this.width; j++) {
          result += 'X';
        }
        console.log(result);
      }
    }
  
    rotate () {
      [this.width, this.height] = [this.height, this.width];
    }
  
    double () {
      this.width = 2 * this.width;
      this.height = 2 * this.height;
    }
};
