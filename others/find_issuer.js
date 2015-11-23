var issuerRange = {};
var issuerLen = {},
    maxLen = 0;

var add = function(ranges, issuer, lenRanges) {
    ranges.forEach(function(item) {
        maxLen = ((maxLen < item.length) ? item.length : maxLen);
        issuerRange[item] = issuer;
    });
    issuerLen[issuer] = lenRanges;
};

add(['4026', '417500', '4405', '4508', '4844', '4913', '4917'], 'VISAELECTRON', [16]);
add(['4'], 'VISA', [13, 16]);
add(['34', '37'], 'AMEX', [15]);
add(['36'], 'DC', [14]);

function isVisaElectron(cc) {
    var four = cc.substr(0, 4);
    six = cc.substr(0, 6),
        ranges = issuerRange['VISAELECTRON'];
    return (issuerRange[four] || issuerRange[six]);
}

function getIssuer(cc) {
    if(typeof cc == 'undefined'){
        return 'NOT APPLICABLE';
    }
    var prefix = '';
    for (var i = 0; i < maxLen; i++) {
        prefix += cc[i];
        var issuer = issuerRange[ prefix ];
        if (issuer && issuerLen[issuer].indexOf( cc.length ) >= 0) {
            if (issuer === 'VISA') {
                issuer = (isVisaElectron(cc) ? 'VISAELECTRON' : 'VISA');
            }
            return issuer;
        }
    }
    return 'UNAVAILABLE';
}


function assertEqual(cc, expectedIssuer) {
    var actualIssuer = getIssuer(cc);
    if (actualIssuer !== expectedIssuer) {
        throw new Error("test failed expectedIssuer for " + cc + " was " + expectedIssuer + " and actual issuer was " + actualIssuer);
    }
    return true;
}

assertEqual('346416800707698', 'AMEX');
assertEqual('376416800707698', 'AMEX');
assertEqual('37641680070769832112', 'UNAVAILABLE');
assertEqual('36641680070769', 'DC');
assertEqual('54545641680070769', 'UNAVAILABLE');
assertEqual('4175004175004172', 'VISAELECTRON');
assertEqual('4917491749174917', 'VISAELECTRON');
assertEqual('4111111111111111', 'VISA');
console.log('done');
