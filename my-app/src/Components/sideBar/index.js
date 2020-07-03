import React from "react";

import Logo from "../Logo";
import NavButton from "../navButton";

import homeIcon from "../../img/homeIcon.svg";
import metaIcon from "../../img/metasIcon.svg";
import relatorioIcon from "../../img/relatorioIcon.svg";
import analiseIcon from "../../img/analiseIcon.svg";
import funcIcon from "../../img/funcIcon.svg";

import style from "../sideBar/sibeBar.module.css";

function sideBar() {
  return (
    <div className={style.sideBar}>
      <Logo />
      <NavButton
        className={style.inicio}
        text="Início"
        iconUrl={homeIcon}
        url="/"
      />
      <NavButton text="Meta" iconUrl={metaIcon} url="/" />
      <NavButton text="Relatório" iconUrl={relatorioIcon} url="/" />
      <NavButton text="Análise" iconUrl={analiseIcon} url="/" />
      <NavButton text="Quadro de Func" iconUrl={funcIcon} url="/" />
    </div>
  );
}

export default sideBar;
