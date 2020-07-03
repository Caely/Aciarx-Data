import React from "react";

import style from "./main.module.css";

function Main({ children, ...otherProps }) {
  return (
    <div className={style.main} {...otherProps}>
      <div className={style.content} children={children} />
    </div>
  );
}

export default Main;
