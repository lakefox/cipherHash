# cipherHash
Custom Encryption Algrothim Used in IXO.js

# How to Use
``` javascript
// Load the module
var c = require("cipherHash");

// Encrypt a String

c.cipherHash("message", "password");

>>> "30A1Dd4XQawUdz"
  
// Decrypt a String

c.UnCipherHash("30A1Dd4XQawUdz", "password");

```