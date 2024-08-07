import path from "../gulpconfig/path.js";

import del from "del";

const clear = () => {
    return del(path.root);
}

export default clear;
