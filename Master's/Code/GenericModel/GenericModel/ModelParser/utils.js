'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});
/**
 * @function detectType
 * Detects the type of the graph text.
 * ```mermaid
 * graph LR
 *  a-->b
 *  b-->c
 *  c-->d
 *  d-->e
 *  e-->f
 *  f-->g
 *  g-->h
 * ```
 *
 * @param {string} text The text defining the graph
 * @returns {string} A graph definition key
 */
var detectType = exports.detectType = function detectType(text) {
    text = text.replace(/^\s*%%.*\n/g, '\n');
    if (text.match(/^\s*sequenceDiagram/)) {
        return 'sequenceDiagram';
    }

    if (text.match(/^\s*digraph/)) {
        return 'dotGraph';
    }

    if (text.match(/^\s*info/)) {
        return 'info';
    }

    if (text.match(/^\s*gantt/)) {
        return 'gantt';
    }

    if (text.match(/^\s*classDiagram/)) {
        return 'classDiagram';
    }

    if (text.match(/^\s*gitGraph/)) {
        return 'gitGraph';
    }
    return 'graph';
};

/**
 * @function isSubstringInArray
 * Detects whether a substring in present in a given array
 * @param {string} str The substring to detect
 * @param {array} arr The array to search
 * @returns {number} the array index containing the substring or -1 if not present
 **/
var isSubstringInArray = exports.isSubstringInArray = function isSubstringInArray(str, arr) {
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].match(str)) return i;
    }
    return -1;
};

exports.default = {
    detectType: detectType,
    isSubstringInArray: isSubstringInArray
};