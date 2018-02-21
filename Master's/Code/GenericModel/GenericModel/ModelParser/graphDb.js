'use strict';

Object.defineProperty(exports, "__esModule", {
    value: true
});
exports.getSubGraphs = exports.indexNodes = exports.getDepthFirstPos = exports.addSubGraph = exports.defaultStyle = exports.clear = exports.getClasses = exports.getEdges = exports.getVertices = exports.getDirection = exports.bindFunctions = exports.setClickEvent = exports.getTooltip = exports.setClass = exports.setDirection = exports.addClass = exports.updateLink = exports.updateLinkInterpolate = exports.addLink = exports.addVertex = undefined;

var _typeof = typeof Symbol === "function" && typeof Symbol.iterator === "symbol" ? function (obj) { return typeof obj; } : function (obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; };

var _utils = require('./utils');

var _utils2 = _interopRequireDefault(_utils);

var _d = require('./d3');

var _d2 = _interopRequireDefault(_d);

function _interopRequireDefault(obj) {
    console.log(obj);
    return obj && obj.__esModule ? obj : { default: obj };
}

var vertices = {};
var edges = [];
var classes = [];
var subGraphs = [];
var tooltips = {};
var subCount = 0;
var direction = void 0;
// Functions to be run after graph rendering
var funs = [];
/**
 * Function called by parser when a node definition has been found
 * @param id
 * @param text
 * @param type
 * @param style
 */
var addVertex = exports.addVertex = function addVertex(id, text, type, style) {
    var txt = void 0;

    if (typeof id === 'undefined') {
        return;
    }
    if (id.trim().length === 0) {
        return;
    }

    if (typeof vertices[id] === 'undefined') {
        vertices[id] = { id: id, styles: [], classes: [] };
    }
    if (typeof text !== 'undefined') {
        txt = text.trim();

        // strip quotes if string starts and exnds with a quote
        if (txt[0] === '"' && txt[txt.length - 1] === '"') {
            txt = txt.substring(1, txt.length - 1);
        }

        vertices[id].text = txt;
    }
    if (typeof type !== 'undefined') {
        vertices[id].type = type;
    }
    if (typeof type !== 'undefined') {
        vertices[id].type = type;
    }
    if (typeof style !== 'undefined') {
        if (style !== null) {
            style.forEach(function (s) {
                vertices[id].styles.push(s);
            });
        }
    }
};

/**
 * Function called by parser when a link/edge definition has been found
 * @param start
 * @param end
 * @param type
 * @param linktext
 */
var addLink = exports.addLink = function addLink(start, end, type, linktext) {
    var edge = { start: start, end: end, type: undefined, text: '' };
    linktext = type.text;

    if (typeof linktext !== 'undefined') {
        edge.text = linktext.trim();

        // strip quotes if string starts and exnds with a quote
        if (edge.text[0] === '"' && edge.text[edge.text.length - 1] === '"') {
            edge.text = edge.text.substring(1, edge.text.length - 1);
        }
    }

    if (typeof type !== 'undefined') {
        edge.type = type.type;
        edge.stroke = type.stroke;
    }
    edges.push(edge);
};

/**
 * Updates a link's line interpolation algorithm
 * @param pos
 * @param interpolate
 */
var updateLinkInterpolate = exports.updateLinkInterpolate = function updateLinkInterpolate(pos, interp) {
    if (pos === 'default') {
        edges.defaultInterpolate = interp;
    } else {
        edges[pos].interpolate = interp;
    }
};

/**
 * Updates a link with a style
 * @param pos
 * @param style
 */
var updateLink = exports.updateLink = function updateLink(pos, style) {
    if (pos === 'default') {
        edges.defaultStyle = style;
    } else {
        if (_utils2.default.isSubstringInArray('fill', style) === -1) {
            style.push('fill:none');
        }
        edges[pos].style = style;
    }
};

var addClass = exports.addClass = function addClass(id, style) {
    if (typeof classes[id] === 'undefined') {
        classes[id] = { id: id, styles: [] };
    }

    if (typeof style !== 'undefined') {
        if (style !== null) {
            style.forEach(function (s) {
                classes[id].styles.push(s);
            });
        }
    }
};

/**
 * Called by parser when a graph definition is found, stores the direction of the chart.
 * @param dir
 */
var setDirection = exports.setDirection = function setDirection(dir) {
    direction = dir;
};

/**
 * Called by parser when a graph definition is found, stores the direction of the chart.
 * @param dir
 */
var setClass = exports.setClass = function setClass(id, className) {
    if (id.indexOf(',') > 0) {
        id.split(',').forEach(function (id2) {
            if (typeof vertices[id2] !== 'undefined') {
                vertices[id2].classes.push(className);
            }
        });
    } else {
        if (typeof vertices[id] !== 'undefined') {
            vertices[id].classes.push(className);
        }
    }
};

var setTooltip = function setTooltip(id, tooltip) {
    if (typeof tooltip !== 'undefined') {
        tooltips[id] = tooltip;
    }
};

var setClickFun = function setClickFun(id, functionName) {
    if (typeof functionName === 'undefined') {
        return;
    }
    if (typeof vertices[id] !== 'undefined') {
        funs.push(function (element) {
            var elem = _d2.default.select(element).select('#' + id);
            if (elem !== null) {
                elem.on('click', function () {
                    window[functionName](id);
                });
            }
        });
    }
};

var setLink = function setLink(id, linkStr) {
    if (typeof linkStr === 'undefined') {
        return;
    }
    if (typeof vertices[id] !== 'undefined') {
        funs.push(function (element) {
            var elem = _d2.default.select(element).select('#' + id);
            if (elem !== null) {
                elem.on('click', function () {
                    window.open(linkStr, 'newTab');
                });
            }
        });
    }
};
var getTooltip = exports.getTooltip = function getTooltip(id) {
    return tooltips[id];
};

/**
 * Called by parser when a graph definition is found, stores the direction of the chart.
 * @param dir
 */
var setClickEvent = exports.setClickEvent = function setClickEvent(id, functionName, link, tooltip) {
    if (id.indexOf(',') > 0) {
        id.split(',').forEach(function (id2) {
            setTooltip(id2, tooltip);
            setClickFun(id2, functionName);
            setLink(id2, link);
            setClass(id, 'clickable');
        });
    } else {
        setTooltip(id, tooltip);
        setClickFun(id, functionName);
        setLink(id, link);
        setClass(id, 'clickable');
    }
};

var bindFunctions = exports.bindFunctions = function bindFunctions(element) {
    funs.forEach(function (fun) {
        fun(element);
    });
};
var getDirection = exports.getDirection = function getDirection() {
    return direction;
};
/**
 * Retrieval function for fetching the found nodes after parsing has completed.
 * @returns {{}|*|vertices}
 */
var getVertices = exports.getVertices = function getVertices() {
    return vertices;
};

/**
 * Retrieval function for fetching the found links after parsing has completed.
 * @returns {{}|*|edges}
 */
var getEdges = exports.getEdges = function getEdges() {
    return edges;
};

/**
 * Retrieval function for fetching the found class definitions after parsing has completed.
 * @returns {{}|*|classes}
 */
var getClasses = exports.getClasses = function getClasses() {
    return classes;
};

var setupToolTips = function setupToolTips(element) {
    var tooltipElem = _d2.default.select('.mermaidTooltip');
    if (tooltipElem[0][0] === null) {
        tooltipElem = _d2.default.select('body').append('div').attr('class', 'mermaidTooltip').style('opacity', 0);
    }

    var svg = _d2.default.select(element).select('svg');

    var nodes = svg.selectAll('g.node');
    nodes.on('mouseover', function () {
        var el = _d2.default.select(this);
        var title = el.attr('title');
        // Dont try to draw a tooltip if no data is provided
        if (title === null) {
            return;
        }
        var rect = this.getBoundingClientRect();

        tooltipElem.transition().duration(200).style('opacity', '.9');
        tooltipElem.html(el.attr('title')).style('left', rect.left + (rect.right - rect.left) / 2 + 'px').style('top', rect.top - 14 + document.body.scrollTop + 'px');
        el.classed('hover', true);
    }).on('mouseout', function () {
        tooltipElem.transition().duration(500).style('opacity', 0);
        var el = _d2.default.select(this);
        el.classed('hover', false);
    });
};
funs.push(setupToolTips);

/**
 * Clears the internal graph db so that a new graph can be parsed.
 */
var clear = exports.clear = function clear() {
    vertices = {};
    classes = {};
    edges = [];
    funs = [];
    funs.push(setupToolTips);
    subGraphs = [];
    subCount = 0;
    tooltips = [];
};
/**
 *
 * @returns {string}
 */
var defaultStyle = exports.defaultStyle = function defaultStyle() {
    return 'fill:#ffa;stroke: #f66; stroke-width: 3px; stroke-dasharray: 5, 5;fill:#ffa;stroke: #666;';
};

/**
 * Clears the internal graph db so that a new graph can be parsed.
 */
var addSubGraph = exports.addSubGraph = function addSubGraph(list, title) {
    function uniq(a) {
        var prims = { 'boolean': {}, 'number': {}, 'string': {} };
        var objs = [];

        return a.filter(function (item) {
            var type = typeof item === 'undefined' ? 'undefined' : _typeof(item);
            if (item === ' ') {
                return false;
            }
            if (type in prims) {
                return prims[type].hasOwnProperty(item) ? false : prims[type][item] = true;
            } else {
                return objs.indexOf(item) >= 0 ? false : objs.push(item);
            }
        });
    }

    var nodeList = [];

    nodeList = uniq(nodeList.concat.apply(nodeList, list));

    var subGraph = { id: 'subGraph' + subCount, nodes: nodeList, title: title };
    subGraphs.push(subGraph);
    subCount = subCount + 1;
    return subGraph.id;
};

var getPosForId = function getPosForId(id) {
    for (var i = 0; i < subGraphs.length; i++) {
        if (subGraphs[i].id === id) {
            return i;
        }
    }
    return -1;
};
var secCount = -1;
var posCrossRef = [];
var indexNodes2 = function indexNodes2(id, pos) {
    var nodes = subGraphs[pos].nodes;
    secCount = secCount + 1;
    if (secCount > 2000) {
        return;
    }
    posCrossRef[secCount] = pos;
    // Check if match
    if (subGraphs[pos].id === id) {
        return {
            result: true,
            count: 0
        };
    }

    var count = 0;
    var posCount = 1;
    while (count < nodes.length) {
        var childPos = getPosForId(nodes[count]);
        // Ignore regular nodes (pos will be -1)
        if (childPos >= 0) {
            var res = indexNodes2(id, childPos);
            if (res.result) {
                return {
                    result: true,
                    count: posCount + res.count
                };
            } else {
                posCount = posCount + res.count;
            }
        }
        count = count + 1;
    }

    return {
        result: false,
        count: posCount
    };
};

var getDepthFirstPos = exports.getDepthFirstPos = function getDepthFirstPos(pos) {
    return posCrossRef[pos];
};
var indexNodes = exports.indexNodes = function indexNodes() {
    secCount = -1;
    if (subGraphs.length > 0) {
        indexNodes2('none', subGraphs.length - 1, 0);
    }
};

var getSubGraphs = exports.getSubGraphs = function getSubGraphs() {
    return subGraphs;
};

exports.default = {
    addVertex: addVertex,
    addLink: addLink,
    updateLinkInterpolate: updateLinkInterpolate,
    updateLink: updateLink,
    addClass: addClass,
    setDirection: setDirection,
    setClass: setClass,
    getTooltip: getTooltip,
    setClickEvent: setClickEvent,
    bindFunctions: bindFunctions,
    getDirection: getDirection,
    getVertices: getVertices,
    getEdges: getEdges,
    getClasses: getClasses,
    clear: clear,
    defaultStyle: defaultStyle,
    addSubGraph: addSubGraph,
    getDepthFirstPos: getDepthFirstPos,
    indexNodes: indexNodes,
    getSubGraphs: getSubGraphs
};