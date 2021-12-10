db.createCollection("counter")
db.counter.insert({_id: "nameID", seq: 0});
function nextVal(name) {
    var ret = db.counter.findAndModify(
        {
            query: { _id: name },
            update: { $inc: { seq: 1 } },
            new: true
        });
    return ret.seq;
 };