<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1u-ewO-2_H37_lNGG7F81YmKRR4zkwmlR -->
<html lang="en" theme="dark" class="cell-ui-refresh" editor="Default Dark" style="--colab-code-font-size: 18px;"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="meshmuth18@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./4app_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-zyrznN4OCDIFU1vyQsy7yYiQl77TkF1g9adpwZrWl4U0/QJEyx4b0r1P0UMwLEKw" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./4app_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-zyrznN4OCDIFU1vyQsy7yYiQl77TkF1g9adpwZrWl4U0/QJEyx4b0r1P0UMwLEKw" nonce=""></script><script src="./4app_files/cb=gapi.loaded_1" nonce="" async=""></script><script type="text/javascript" async="" src="./4app_files/js" nonce=""></script><script src="./4app_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./4app_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>app.py - Colab</title><link href="./4app_files/css2" rel="stylesheet"><link href="./4app_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_ub{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none;user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta,.gb_Ua{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua,#gb a.gb_Ua{color:#666;cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:-webkit-gradient(linear,left top,left bottom,from(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(to bottom,#4387fd,#4683ea)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:-webkit-gradient(linear,left top,left bottom,from(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(to bottom,#3c7ae4,#3f76d3)}#gb .gb_Va{background:#ffffff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_td{display:inline-block;padding:4px 4px 4px 4px;vertical-align:middle}.gb_ud .gb_Q{bottom:-3px;right:-5px}.gb_td:first-child,#gbsfw:first-child+.gb_td{padding-left:0}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px}.gb_B,#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_vd,.gb_wd{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:6.5px;top:37px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_wd{border-bottom-color:#ccc;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_wd{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-moz-user-select:text;-ms-user-select:text;-webkit-user-select:text}.gb_td.gb_8c .gb_vd,.gb_td.gb_8c .gb_wd,.gb_td.gb_8c .gb_la,.gb_8c.gb_la{display:block}.gb_td.gb_8c.gb_xd .gb_vd,.gb_td.gb_8c.gb_xd .gb_wd{display:none}.gb_yd{position:absolute;right:8px;top:62px;z-index:-1}.gb_kb .gb_vd,.gb_kb .gb_wd,.gb_kb .gb_la{margin-top:-10px}.gb_td:first-child,#gbsfw:first-child+.gb_td{padding-left:4px}.gb_Fa.gb_zd .gb_td:first-child{padding-left:0}.gb_Ad{position:relative}.gb_gd .gb_Ad,.gb_Bd .gb_Ad{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_Cd:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;border-radius:50%}.gb_Dd button svg,.gb_B{border-radius:50%}.gb_Dd button:focus:not(:focus-visible) svg,.gb_Dd button:hover svg,.gb_Dd button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_0c .gb_Dd.gb_Ed button:focus-visible svg,.gb_Dd button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_0c .gb_Dd button:focus-visible svg,.gb_0c .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_0c .gb_Dd.gb_Ed button:focus-visible svg,.gb_Dd button:focus-visible svg,.gb_0c .gb_Dd button:focus-visible svg{outline:1px solid currentcolor}}.gb_0c .gb_Dd.gb_Ed button:focus svg,.gb_0c .gb_Dd.gb_Ed button:focus:hover svg,.gb_Dd button:focus svg,.gb_Dd button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_0c .gb_Dd.gb_Ed button:active svg,.gb_Dd button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_0c .gb_Dd.gb_Ed button:hover svg,.gb_Dd button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_0c .gb_Dd button:hover svg,.gb_0c .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_0c .gb_Dd button:focus svg,.gb_0c .gb_Dd button:focus:hover svg,.gb_0c .gb_B:focus,.gb_0c .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_0c .gb_Dd button:active svg,.gb_0c .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_0c .gb_B[aria-expanded=true],.gb_0c .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_0c .gb_B[aria-expanded=true] .gb_F{fill:#ffffff;opacity:1}.gb_td{padding:4px}.gb_Fa.gb_zd .gb_td{padding:4px 2px}.gb_Fa.gb_zd .gb_z.gb_td{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_Fd{left:0;right:auto}@media (max-width:350px){.gb_la.gb_Fd{left:0}}.gb_Hd .gb_la{top:56px}.gb_R{display:none!important}.gb_eb{visibility:hidden}.gb_J .gb_B{background-position:-64px -29px;opacity:.55}.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_Id:not(.gb_Jd) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_nd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_nd.gb_od{color:#3c4043}.gb_Fa.gb_oc .gb_nd{margin-bottom:0}.gb_pd.gb_qd .gb_nd{padding-left:4px}.gb_Fa.gb_oc .gb_rd{position:relative;top:-2px}.gb_sd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow .25s;transition:box-shadow .25s}.gb_Fa.gb_7c{min-width:120px}.gb_Fa.gb_Pd .gb_Qd{display:none}.gb_Fa.gb_Pd .gb_Id{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Rd{position:fixed;top:0;width:100%}.gb_Sd{box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Td{height:64px}.gb_Id{box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:justify;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_oc) .gb_Id{padding:8px}.gb_Fa.gb_Vd .gb_Id{-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Fa .gb_Id.gb_Jd.gb_Wd{min-width:0}.gb_Fa.gb_oc .gb_Id{padding:4px;padding-left:8px;min-width:0}.gb_Qd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none;user-select:none}.gb_Xd>.gb_Qd{display:table-cell;width:100%}.gb_pd{padding-right:30px;box-sizing:border-box;-webkit-box-flex:1;-webkit-flex:1 0 auto;flex:1 0 auto}.gb_Fa.gb_oc .gb_pd{padding-right:14px}.gb_Zd{-webkit-box-flex:1;-webkit-flex:1 1 100%;flex:1 1 100%}.gb_Zd>:only-child{display:inline-block}.gb_0d.gb_hd{padding-left:4px}.gb_0d.gb_1d,.gb_Fa.gb_Vd .gb_0d,.gb_Fa.gb_oc:not(.gb_Bd) .gb_0d{padding-left:0}.gb_Fa.gb_oc .gb_0d.gb_1d{padding-right:0}.gb_Fa.gb_oc .gb_0d.gb_1d .gb_Wa{margin-left:10px}.gb_hd{display:inline}.gb_Fa.gb_bd .gb_0d.gb_2d,.gb_Fa.gb_Bd .gb_0d.gb_2d{padding-left:2px}.gb_nd{display:inline-block}.gb_0d{box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-box-flex:0;-webkit-flex:0 0 auto;flex:0 0 auto;-webkit-box-pack:end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Bd{height:48px}.gb_Fa.gb_Bd{min-width:auto}.gb_Bd .gb_0d{float:right;padding-left:32px}.gb_Bd .gb_0d.gb_3d{padding-left:0}.gb_4d{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text;user-select:text}.gb_Ld{-webkit-transition:background-color .4s;transition:background-color .4s}.gb_7d{color:black}.gb_0c{color:white}.gb_Fa a,.gb_4c a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_4c svg,.gb_pd .gb_Od,.gb_gd .gb_Od{color:#5f6368;opacity:1}.gb_0c svg,.gb_4c.gb_9c svg{color:rgba(255,255,255,.87)}.gb_0c .gb_pd .gb_Od,.gb_0c .gb_pd .gb_Zc,.gb_0c .gb_pd .gb_rd,.gb_4c.gb_9c .gb_Od{color:rgba(255,255,255,.87)}.gb_0c .gb_pd .gb_Xc:not(.gb_8d){opacity:.87}.gb_od{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.gb_0c .gb_od,.gb_7d .gb_od{opacity:1}.gb_5d{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_0c a.gb_X,.gb_0c span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_Md{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Bd .gb_Md{margin-left:8px}#gb a.gb_Ua.gb_Md{cursor:pointer}.gb_Ua.gb_Md:hover{background:#1b66c9;box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_Md:focus,.gb_Ua.gb_Md:hover:focus{background:#1c5fba;box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_Md:active{background:#1b63c1;box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Md{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_oc .gb_Md{padding:9px 15px;min-width:80px}.gb_6d{text-align:left}#gb .gb_0c a.gb_Md:not(.gb_H),#gb.gb_0c a.gb_Md{background:#fff;border-color:#dadce0;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_Md{background:#8ab4f8;border:1px solid transparent;box-shadow:none;color:#202124}#gb .gb_0c a.gb_Md:hover:not(.gb_H),#gb.gb_0c a.gb_Md:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_Md:hover{background:#93baf9;border-color:transparent;box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_0c a.gb_Md:focus:not(.gb_H),#gb .gb_0c a.gb_Md:focus:hover:not(.gb_H),#gb.gb_0c a.gb_Md:focus:not(.gb_H),#gb.gb_0c a.gb_Md:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_Md:focus,#gb a.gb_Ua.gb_H.gb_Md:focus:hover{background:#a6c6fa;border-color:transparent;box-shadow:none}#gb .gb_0c a.gb_Md:active:not(.gb_H),#gb.gb_0c a.gb_Md:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_Md:active{background:#a1c3f9;box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_Id .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_8c.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Vc{vertical-align:middle}.gb_Fa:not(.gb_oc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_9d{max-height:32px;width:78px}.gb_Wa.gb_H .gb_9d{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_fb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_fb.gb_P{height:30px;width:30px}.gb_fb.gb_P:hover,.gb_fb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_gb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px;line-height:normal;z-index:1}.gb_hb{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_ib::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_ib::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_jb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_jb{width:auto}.gb_jb:hover,.gb_jb:focus{opacity:.85}.gb_kb .gb_jb,.gb_kb .gb_lb{line-height:26px}#gb#gb.gb_kb a.gb_jb,.gb_kb .gb_lb{font-size:11px;height:auto}.gb_mb{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_mb{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_nb.gb_eb{color:#fff}.gb_1 .gb_jb,.gb_1 .gb_mb{opacity:1}#gb#gb.gb_1.gb_1 a.gb_jb,#gb#gb .gb_1.gb_1 a.gb_jb{color:#fff}.gb_1.gb_1 .gb_mb{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_ob .gb_z,.gb_pb .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_qb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_rb.gb_sb .gb_jb{width:30px!important}.gb_tb{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_ub .gb_tb,.gb_vb .gb_tb{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.Z-yMYH2MhSc.2019.O","co.ke","en-GB","425",0,[4,2,"","","","804219421","0"],null,"GZPCaMuvCP3E6-APpZPJsQI",null,0,"og.qtm.mNmoKZZmNuE.L.W.O","AA2YrTv7FsbgCKTX-W0ZX0KlDh9w0jgxxg","AA2YrTuCFsUYSdxg8eKTAzlgJ62hYMQ54w","",2,1,200,"KEN",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","meshmuth18@gmail.com","","AIhRldIrZRyflqtTSJI55mNHK8FhUGmVXD9bYsJXZZAgCGNge8CzsSyw_RMiUlbl4zqybqEHt-nsPfS0vP8Bum9MQPZEVUcJtw",0,0,null,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",1,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.GJa4oir6WlA.O/d=1/rs=AHpOoo-oT18V72om9ubISB9Na8GvbQT5cg/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250803.0_p0","en-GB",null,0],[0.009999999776482582,"co.ke","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"KEN","en-GB","804219421.0",8,null,1,0,null,null,null,null,"105109531,105109534",null,null,null,"GZPCaMuvCP3E6-APpZPJsQI",0,0,0,null,2,5,"nn",50,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.Z-yMYH2MhSc.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTv7FsbgCKTX-W0ZX0KlDh9w0jgxxg"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.mNmoKZZmNuE.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTuCFsUYSdxg8eKTAzlgJ62hYMQ54w"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?baea=1\u0026amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,1,0],0,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en-GB",0,["https://colab.research.google.com/?authuser=$authuser","https://accounts.google.com/AddSession?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en-GB\u0026continue=https://colab.research.google.com/\u0026timeStmp=1757582105\u0026secTok=.AG5fkS_DNu56P6lcHehUkcPCZpBIgwXtoA\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026authuser=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2F\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","19024362-1:","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"8559284470",3,1,0],0,null,null,null,1,0,"meshmuth18@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,$a,cb,eb,jb,fb,lb,rb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.zk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.fa[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.Qa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Ra=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Sa=function(a){return a==null||typeof a==="string"?a:void 0};_.Va=function(a,b,c){if(a!=null&&a[_.Ta]===_.Ua)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Ya=function(a){const b=_.Wa(_.Xa);return b?a[b]:void 0};$a=function(a,b){b<100||_.Ja(Za,1)};
cb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Wa(_.Xa),g;!e&&f&&(g=a[f])&&g.xd($a);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=ab)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const D=r-p;var q=void 0;((q=b)!=null?q:b={})[D]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let D;if(m&&!Number.isNaN(h)&&(D=h+p)<g)f[D]=q;else{let Q;((Q=b)!=null?Q:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Wa(_.Xa)&&(a=_.Ya(a))&&"function"==typeof _.bb&&a instanceof _.bb&&(f[_.Xa]=a.i());return f};
eb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.db)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:cb(a,b,eb)}if(a!=null&&a[_.Ta]===_.Ua)return fb(a);if("function"==typeof _.gb&&a instanceof _.gb)return a.j();return}return a};jb=function(a,b){if(b){ab=b==null||b===Fa||b[hb]!==ib?Fa:b;try{return fb(a)}finally{ab=void 0}}return fb(a)};
fb=function(a){a=a.fa;return cb(a,a[_.v]|0,eb)};
_.mb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-8380417|(b&1023)<<13)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(kb&&1&e)throw Error("m");2048&e&&!(2&e)&&lb();if(e&256)throw Error("n");if(e&64)return d!==0||e&2048||(a[_.v]=e|2048),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<
g)c[f+b]=k[h],delete k[h];else break;e=e&-8380417|(g&1023)<<13;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-8380417|(h&1023)<<13}}}e|=64;d===0&&(e|=2048);a[_.v]=e;return a};lb=function(){if(kb)throw Error("p");_.Ja(nb,5)};
rb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.ob(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Ta]===_.Ua)return b=a.fa,c=b[_.v]|0,_.Ea(a,c)?a:_.pb(a,b,c)?_.qb(a,b):_.ob(b,c);if("function"==typeof _.gb&&a instanceof _.gb)return a};_.qb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.ob=function(a,b,c,d){d!=null||(d=!!(34&b));a=cb(a,b,rb,d);d=32;c&&(d|=2);b=b&8380609|d;a[_.v]=b;return a};_.tb=function(a){const b=a.fa,c=b[_.v]|0;return _.Ea(a,c)?_.pb(a,b,c)?_.qb(a,b,!0):new a.constructor(_.ob(b,c,!1)):a};_.ub=function(a){if(a.j!==Da)return!1;var b=a.fa;b=_.ob(b,b[_.v]|0);b[_.v]|=2048;a.fa=b;a.j=void 0;a.o=void 0;return!0};_.vb=function(a){if(!_.ub(a)&&_.Ea(a,a.fa[_.v]|0))throw Error();};_.wb=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.pb=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.xb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>13&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.zb=function(a,b,c,d,e){let f=!1;d=_.yb(a,d,e,g=>{const h=_.Va(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.wb(a,b),d};_.Ab=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};Db=Object.defineProperty;
Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};Gb("globalThis",function(a){return a||Fb});
Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});Gb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Gb("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a,b){var c=_.Ib("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Wa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.nk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>15&1),Qb=!!(Kb[0]&1024),Rb=!!(Kb[0]>>16&1),Sb=!!(Kb[0]&128);var Tb=Jb(1,!0),na=Pb?Rb:Jb(610401301,!1),kb=Pb?Qb||!Sb:Jb(748402147,Tb);_.Ub=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Xb,Vb,Yb,Wb;_.db=_.ba(a=>fa?a>=Vb&&a<=Wb:a[0]==="-"?ja(a,Xb):ja(a,Yb));Xb=Number.MIN_SAFE_INTEGER.toString();Vb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Yb=Number.MAX_SAFE_INTEGER.toString();Wb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Zb=typeof TextDecoder!=="undefined";_.$b=typeof TextEncoder!=="undefined";var oa,ac=_.t.navigator;oa=ac?ac.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.bc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.cc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.dc=function(a){_.dc[" "](a);return a};_.dc[" "]=function(){};var rc;_.ec=_.ra();_.fc=_.sa();_.hc=_.u("Edge");_.ic=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.jc=_.ma()&&!_.u("Edge");_.kc=_.za();_.lc=wa()?oa.platform==="Windows":_.u("Windows");_.mc=wa()?oa.platform==="Android":_.u("Android");_.nc=xa();_.oc=_.u("iPad");_.pc=_.u("iPod");_.qc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.ic)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.hc)return/Edge\/([\d\.]+)/.exec(c);if(_.fc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.jc)return/WebKit\/(\S+)/.exec(c);if(_.ec)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.fc){var sc;const c=_.t.document;sc=c?c.documentMode:void 0;if(sc!=null&&sc>parseFloat(a)){rc=String(sc);break a}}rc=a}_.tc=rc;_.uc=_.ta();_.vc=xa()||_.u("iPod");_.wc=_.u("iPad");_.xc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.yc=ua();_.zc=_.va()&&!_.ya();var Za,nb,hb;_.Xa=_.Ca();_.Ac=_.Ca();Za=_.Ca();_.Bc=_.Ca();nb=_.Ca();_.Ta=_.Ca("m_m",!0);hb=_.Ca();_.Cc=_.Ca();var Ec;_.v=_.Ca("jas",!0);Ec=[];Ec[_.v]=7;_.Dc=Object.freeze(Ec);var Da;_.Ua={};Da={};_.Fc=Object.freeze({});var ib={};var Ia=void 0;_.Gc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Hc=Number.isSafeInteger;_.Na=Number.isFinite;_.Ic=Math.trunc;var ab;_.Jc=_.ia(0);_.Kc={};_.Lc=function(a,b,c,d,e){b=_.yb(a.fa,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.yb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Mc=function(a,b,c,d){_.vb(a);const e=a.fa;_.xb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.fa,f=e[_.v]|0;b=_.zb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.tb(b);g!==b&&(_.ub(a)&&(e=a.fa,f=e[_.v]|0),b=g,f=_.xb(e,f,c,b,d),_.wb(e,f))}return b};_.E=function(a,b,c){c==null&&(c=void 0);_.Mc(a,b,c);c&&!_.Ea(c)&&_.wb(a.fa);return a};_.Nc=function(a,b,c,d){return _.Pa(_.Lc(a,b,c,d))};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Lc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Sa(_.Lc(a,b,d)))!=null?e:c};
_.I=function(a,b,c){return _.Sa(_.Lc(a,b,c,_.Kc))};_.J=function(a,b,c,d){return _.Mc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Mc(a,b,c==null?c:_.Qa(c))};_.L=function(a,b,c,d){return _.Mc(a,b,_.Ra(c),d)};_.N=function(a,b,c,d){return _.Mc(a,b,c==null?c:_.Oa(c),d)};_.O=class{constructor(a,b,c){this.fa=_.mb(a,b,c)}toJSON(){return jb(this)}wa(a){return JSON.stringify(jb(this,a))}};_.O.prototype[_.Ta]=_.Ua;_.O.prototype.toString=function(){return this.fa.toString()};_.Oc=_.Ab();_.Qc=_.Ab();_.Rc=_.Ab();_.Sc=Symbol();var Tc=class extends _.O{constructor(a){super(a)}};_.Uc=class extends _.O{constructor(a){super(a)}D(a){return _.K(this,3,a)}};_.Vc=class extends _.O{constructor(a){super(a)}};_.P=function(){this.qa=this.qa;this.Y=this.Y};_.P.prototype.qa=!1;_.P.prototype.isDisposed=function(){return this.qa};_.P.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.P.prototype[Symbol.dispose]=function(){this.dispose()};_.P.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Wc=class extends _.P{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}tb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].tb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Yc=class extends _.P{constructor(){var a=_.Xc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.Zc=class extends _.O{constructor(a){super(a)}};var $c=class extends _.O{constructor(a){super(a)}};var cd;_.ad=function(a,b,c=98,d=new _.Uc){if(a.i){const e=new Tc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.N(e,5,1);_.E(d,40,e);a.i.log(c,d)}};cd=class{constructor(){var a=bd;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Uc){_.ad(this,a,98,c)}};var dd,ed;dd=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.bc(c,b,a)}catch(d){console.error(d)}}}};_.fd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new ed(a,b,c));dd(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.i=a;dd(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.j=a;dd(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
ed=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.gd=a=>{var b="qc";if(a.qc&&a.hasOwnProperty(b))return a.qc;b=new a;return a.qc=b};_.R=class{constructor(){this.v=new _.fd;this.i=new _.fd;this.D=new _.fd;this.B=new _.fd;this.C=new _.fd;this.A=new _.fd;this.o=new _.fd;this.j=new _.fd;this.F=new _.fd;this.G=new _.fd}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.gd(_.R)}};var jd;_.id=function(){return _.C(_.hd,_.Vc,5)};jd=class extends _.O{constructor(a){super(a)}};var kd;window.gbar_&&window.gbar_.CONFIG?kd=window.gbar_.CONFIG[0]||{}:kd=[];_.hd=new jd(kd);var bd;bd=_.C(_.hd,$c,3)||new $c;_.Xc=new cd;_.A("gbar_._DumpException",function(a){_.Xc?_.Xc.log(a):console.error(a)});_.ld=new Yc;var nd;_.od=function(a,b){var c=_.md.i();if(a in c.i){if(c.i[a]!=b)throw new nd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.md=class{constructor(){this.i={};this.j={}}static i(){return _.gd(_.md)}};_.pd=class extends _.aa{constructor(){super()}};nd=class extends _.pd{};_.A("gbar.A",_.fd);_.fd.prototype.aa=_.fd.prototype.then;_.A("gbar.B",_.R);_.R.prototype.ba=_.R.prototype.qa;_.R.prototype.bb=_.R.prototype.O;_.R.prototype.bd=_.R.prototype.P;_.R.prototype.bf=_.R.prototype.K;_.R.prototype.bg=_.R.prototype.M;_.R.prototype.bh=_.R.prototype.L;_.R.prototype.bj=_.R.prototype.Y;_.R.prototype.bk=_.R.prototype.J;_.R.prototype.bl=_.R.prototype.N;_.A("gbar.a",_.R.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var qd=new Wc;_.od("api",qd);
var rd=_.id()||new _.Vc,sd=window,td=_.y(_.I(rd,8));sd.__PVT=td;_.od("eq",_.ld);
}catch(e){_._DumpException(e)}
try{
_.ud=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var vd=class extends _.O{constructor(a){super(a)}};var wd=class extends _.P{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.Ma(_.Lc(a,12))!=null&&(d.dpo=_.x(_.F(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.G(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var xd=_.C(_.hd,_.Zc,14);if(xd){var yd=_.C(_.hd,_.ud,9)||new _.ud,zd=new vd,Bd=new wd;Bd.init(xd,yd,zd);_.od("gs",Bd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_meshmuth18@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./4app_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250909-060057_RC00_804833152'; var colabScsVersion = '23b1e2eaf9889d21b864894937aaeab5'; var hl = 'en-GB'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: false, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_service_client_type\x22: \x22\x22, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allow_subpaths_in_kernel_url\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22bigquery_sql_engine\x22: false, \x22bigquery_sql_engine_library\x22: \x22\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22cell_ui_refresh\x22: true, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22clone_notebook_link\x22: true, \x22cloud_origin\x22: \x22\x22, \x22cloud_run\x22: false, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_autocomplete\x22: false, \x22composer_bigquery_context\x22: false, \x22composer_context_max_variable_length\x22: 500000, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_generated_cell_placement_logic\x22: false, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_show_debug_info\x22: false, \x22composer_show_single_diff_buttons\x22: false, \x22composer_survey\x22: true, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: true, \x22converse_notebook_context_length\x22: 40000, \x22copy_cell_output\x22: false, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22data_inspector\x22: false, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecated_accelerator_models\x22: \x5b\x22V28\x22\x5d, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22disable_text_cell_double_click_presentation_mode\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22dsa_markdown_cells\x22: false, \x22dsa_sample_datasets_toast\x22: true, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_a100_hm\x22: true, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_cell_pair_slides\x22: true, \x22enable_composer_changeset_stacking\x22: false, \x22enable_composer_code_report\x22: false, \x22enable_composer_suggestion_chips\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_edu_subscription_ui\x22: true, \x22enable_improved_composer_context_mentions\x22: false, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: false, \x22kernel_use_connected_endpoint_for_unassign\x22: true, \x22kernel_utils_fetch\x22: false, \x22key_promoter\x22: false, \x22kr\x22: false, \x22light_editor_themes\x22: true, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_ccu_info\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: true, \x22multi_modal_context_for_transform\x22: false, \x22nl2code_missing_imports\x22: true, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22panel_ui_refresh\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prepare_runtime_for_notebook\x22: false, \x22prereq_cells_next_steps\x22: true, \x22presentation_mode_connect_runtime\x22: false, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduced_gemini_sparks\x22: false, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222025.07\x22\x5d, \x22runtime_version_selector\x22: true, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22signup_ccu_increase\x22: true, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22sql_cell\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suggest_plots\x22: true, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_interval_ms\x22: 500, \x22task_service_poll_timeout_ms\x22: 90000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22term4all\x22: true, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_cell_editor_toolbar_exit_button\x22: false, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22trim_filename_extension\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_ai_service\x22: false, \x22use_colab_adk_service\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730177, 20730150, 20730457, 20730324, 20730484, 20730265, 20730454, 20730375, 20730460, 20730479, 20730363, 20730369, 20730183\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_service_client_type\x22: 45723040, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22bigquery_sql_engine\x22: 45697421, \x22bigquery_sql_engine_library\x22: 45700104, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22clone_notebook_link\x22: 45716348, \x22cloud_origin\x22: 45425538, \x22cloud_run\x22: 45697172, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_autocomplete\x22: 45718105, \x22composer_bigquery_context\x22: 45710683, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_generated_cell_placement_logic\x22: 45721730, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_show_debug_info\x22: 45700003, \x22composer_show_single_diff_buttons\x22: 45723066, \x22composer_survey\x22: 45707270, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22converse_notebook_context_length\x22: 45705427, \x22copy_cell_output\x22: 45712093, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecated_accelerator_models\x22: 45724327, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22disable_text_cell_double_click_presentation_mode\x22: 45723721, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22dsa_markdown_cells\x22: 45707419, \x22dsa_sample_datasets_toast\x22: 45682045, \x22embedded_use_websockets\x22: 45691694, \x22enable_a100_hm\x22: 45723321, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_cell_pair_slides\x22: 45719587, \x22enable_composer_changeset_stacking\x22: 45717253, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_edu_subscription_ui\x22: 45693272, \x22enable_improved_composer_context_mentions\x22: 45721452, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22kernel_use_connected_endpoint_for_unassign\x22: 45684913, \x22kernel_utils_fetch\x22: 45708200, \x22key_promoter\x22: 45425570, \x22light_editor_themes\x22: 45721031, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_ccu_info\x22: 45716751, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22multi_modal_context_for_transform\x22: 45687634, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22panel_ui_refresh\x22: 45721124, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prepare_runtime_for_notebook\x22: 45699118, \x22prereq_cells_next_steps\x22: 45640400, \x22presentation_mode_connect_runtime\x22: 45722751, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduced_gemini_sparks\x22: 45719726, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22runtime_version_selector\x22: 45713197, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22signup_ccu_increase\x22: 45689970, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_completion_lsp\x22: 45688254, \x22suggest_plots\x22: 45696393, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_cell_editor_toolbar_exit_button\x22: 45723722, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22trim_filename_extension\x22: 45691676, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_ai_service\x22: 45713338, \x22use_colab_adk_service\x22: 20730464, \x22user_visible_accelerator_models\x22: 45682571, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'meshmuth18@gmail.com'; var colabRenderDataToken = 'AFWLbD2go_vNeoPRfX2Zt4RXiTllBsXfjQGyVUNibkaLEXRYxoaMV7HRzfP7lRZ6dRSXccsSY8KStknmF11ESAypxV9lg8_TjIg06x-M'; var colabConfig = '\x5b\x5b\x22meshmuth18@gmail.com\x22,\x5b1,\x22AHXL0D2MWJ3kuey0UtGlk9uRFlMPSr1c\/kF61WQGyUvDiq+b7Yi0YH4K7EKCFCNED97kEqGLV2w8HsRWNs6A\/dFLXjV5LB6URfoG1O8rtfK7PXSOLJb4AqJJiAGXmfblCu4LEK+ZXLJmFWxh7yYxDuc4CuxHNRp0kcjmvli5dYzUXVrKsGcfWGxOZuDw8d0WJc+wIVDp2oxA38HrMhhce7k6SCxONdxo99lo0h\/yyk6qDklJ4LG6V\/NqTv7+hUtGD3ZY5GehSYQzdWJbOWxdwhkj0vOih7hb+33aagfCp2DUbl7vp8Y9U9A0yFhzYFjBx4GvXxCRJSSc00P4R1Q16S7xNEgR5l+h8ACHtZsQGEWFNydAU266MxQy1w1z3CsflRdOvGup6yy6toJXnSQqc6T1m\/imtO9FhLDnDHTXCqZMnrfCV9tezE45Pm3K9xD6Ow8trUH6FYus7rgzDffrGl4Q4MOcJztoSsY7iFB9ilnFFVV8phFH5LmoynD6N5i6Eo05JQ8Q0HpaAW6vSuEjn37WjE2F093peizVI7VGzxgVgLrJcqyZ3XPTsoPMprRi6h2S9mI0FmCOVzmv2N+kMkwx9eb9rRv+7zwFRH4rAi44tvtmS1lI\/snugGrl1zDT\/BD8LUtkPgzLWrmNNL\/GQpp22dSVvdvAGVDE5nT5bfBktJ7QoWKVdY06XCMj4C07xroXSK7h437CJeSXjXplu2PNdTqKxJzKtwsPJV9TqzJ\/wOU5h82oE6XaY9FnidLIsf5CWYFvARCPYWzYSKRt4XBx3mi6V9pR+VEvhzdB4Bi77SK6elc7y00Uh6Bg\/0uqrG5C55rWEY5ZmbjYV3VI4tDvMEvU\/H9LKr8lssp1FuaGwKjGfCg4kFu8zP3aUgWJGEZysvlhJXMEBnf1yYSq4MbHFjZPRNqbLGkEASOvcYNbSKczEwvFpv9jXFMDzFrdXjUea6IBv81G3fX0AR\/LEfIRcNZ1spSErnxQhTZNDqOYOWienJaY3fttJXPNBXStU1IiIyMtJ7H9SOb6sWnHfGKsviHi0rEDA6BlyXUkngxCyBHO4cbsjVxkI5Q2oo+MdOfu3gm5Qtg3c9uzfFlZteO89PAgUNreGr41P8+xfRwLpRhF3tmRlAOVFYVMbPuHWZb38ccJ0Q7QJTbDFqbvr\/VBV2Bpw1xIMSKPsYKZNfLDLvz3xA\/A28zFMqJmPl0V42v7RWW68oJGYo6YH2+v0vBeHR77pR1A3X4xleGQNF9hS5h8gR6keoYI5f2j9IDLZCQKegDpHp5ZwtbvmU57aIQja\/LhepJA1JF+qXY0iqBrGSJrDyShNntV8yAw+RzoIQwe9aUUQXTqgtjZS0+fDEBLFKAXPl43hfKau\/w00YtEhrygEoHIl7ixZgPkl0hDuPRc+IpufczXaXGqjzaFv3+5U\/+VwEVCB7kRzTLW2qLGy6UHq1yWFepnwkO+RawFRHfkwIzM4AyKlfMP3sLwkatnRK8e51QRB+EObe0r9NW79\/6YQSZriAXNDJtlRzFwB4aeetyjfq84HmSNZKJIjEu8Eb84kXALUWEMHeCbbtvkUClHHBrnAc5rXqSWBNslsJO2Jei3ie7hlPnDHhmYml9cvhyQTTOl4UarAzRtmrGnQkGCxesErbkAQVucYCi8YbQtNjKhpafVOouMRrcwxvLuLlMkvMplnBV9L9l3XWmLTuu+t8b83j2mu4Kt\/eSnA+yVumZLVtv9N6u2pAE\/XMIy5hIqsGrMnUGWTE3FwfDUn4wqXXFYdTtNkFptS6ieJJbr3UmOgxoRhikbS0QBKEe6THyHj0rW7Dasp73k+M0dfXY5klUhDgj2+9FAWY5\/Y6w4AJnLQP\/3qprhgCOI5cjzUmjMgHdwqpXJ\/ONns9yhmo1il1WNdCMwGlH5B37CGA9ihQLK2WMoi\/Ql1J7x\/2u\/8w0jBKlOHeYPROgP5vKmgH01o5ZQbXfic1VbmMmtldVsaT\/bnohq\x22,\x22AJ9oCCwiT8UKycrhCLsmWCP\/1EnzT6AKet8Cp3rHeR8i5oTcDwcMtgUhonk1+yKP+n\/kAl\/uQfS0EPMogt5F8Ckfx4lSsUkFqL10XhwrVp5JDEdgu5ZR0Sh8wXPMIA6ZwEd+mT+3Xb9I\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22$9.99\x22,\x22$49.99\x22,\x22$9.99\x22,\x22$49.99\x22,0,0,0\x5d,\x5b4,5\x5d,\x22KE\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/23b1e2eaf9889d21b864894937aaeab5/img/favicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./4app_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="" type="text/javascript" charset="UTF-8" src="./4app_files/rs=AA2YrTv7FsbgCKTX-W0ZX0KlDh9w0jgxxg" nonce=""></script><link type="text/css" href="./4app_files/rs=AA2YrTuCFsUYSdxg8eKTAzlgJ62hYMQ54w" rel="stylesheet"><style>.swal2-popup.swal2-toast{box-sizing:border-box;grid-column:1/4 !important;grid-row:1/4 !important;grid-template-columns:min-content auto min-content;padding:1em;overflow-y:hidden;background:#fff;box-shadow:0 0 1px rgba(0,0,0,.075),0 1px 2px rgba(0,0,0,.075),1px 2px 4px rgba(0,0,0,.075),1px 3px 8px rgba(0,0,0,.075),2px 4px 16px rgba(0,0,0,.075);pointer-events:all}.swal2-popup.swal2-toast>*{grid-column:2}.swal2-popup.swal2-toast .swal2-title{margin:.5em 1em;padding:0;font-size:1em;text-align:initial}.swal2-popup.swal2-toast .swal2-loading{justify-content:center}.swal2-popup.swal2-toast .swal2-input{height:2em;margin:.5em;font-size:1em}.swal2-popup.swal2-toast .swal2-validation-message{font-size:1em}.swal2-popup.swal2-toast .swal2-footer{margin:.5em 0 0;padding:.5em 0 0;font-size:.8em}.swal2-popup.swal2-toast .swal2-close{grid-column:3/3;grid-row:1/99;align-self:center;width:.8em;height:.8em;margin:0;font-size:2em}.swal2-popup.swal2-toast .swal2-html-container{margin:.5em 1em;padding:0;overflow:initial;font-size:1em;text-align:initial}.swal2-popup.swal2-toast .swal2-html-container:empty{padding:0}.swal2-popup.swal2-toast .swal2-loader{grid-column:1;grid-row:1/99;align-self:center;width:2em;height:2em;margin:.25em}.swal2-popup.swal2-toast .swal2-icon{grid-column:1;grid-row:1/99;align-self:center;width:2em;min-width:2em;height:2em;margin:0 .5em 0 0}.swal2-popup.swal2-toast .swal2-icon .swal2-icon-content{display:flex;align-items:center;font-size:1.8em;font-weight:bold}.swal2-popup.swal2-toast .swal2-icon.swal2-success .swal2-success-ring{width:2em;height:2em}.swal2-popup.swal2-toast .swal2-icon.swal2-error [class^=swal2-x-mark-line]{top:.875em;width:1.375em}.swal2-popup.swal2-toast .swal2-icon.swal2-error [class^=swal2-x-mark-line][class$=left]{left:.3125em}.swal2-popup.swal2-toast .swal2-icon.swal2-error [class^=swal2-x-mark-line][class$=right]{right:.3125em}.swal2-popup.swal2-toast .swal2-actions{justify-content:flex-start;height:auto;margin:0;margin-top:.5em;padding:0 .5em}.swal2-popup.swal2-toast .swal2-styled{margin:.25em .5em;padding:.4em .6em;font-size:1em}.swal2-popup.swal2-toast .swal2-success{border-color:#a5dc86}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-circular-line]{position:absolute;width:1.6em;height:3em;transform:rotate(45deg);border-radius:50%}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-circular-line][class$=left]{top:-0.8em;left:-0.5em;transform:rotate(-45deg);transform-origin:2em 2em;border-radius:4em 0 0 4em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-circular-line][class$=right]{top:-0.25em;left:.9375em;transform-origin:0 1.5em;border-radius:0 4em 4em 0}.swal2-popup.swal2-toast .swal2-success .swal2-success-ring{width:2em;height:2em}.swal2-popup.swal2-toast .swal2-success .swal2-success-fix{top:0;left:.4375em;width:.4375em;height:2.6875em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-line]{height:.3125em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-line][class$=tip]{top:1.125em;left:.1875em;width:.75em}.swal2-popup.swal2-toast .swal2-success [class^=swal2-success-line][class$=long]{top:.9375em;right:.1875em;width:1.375em}.swal2-popup.swal2-toast .swal2-success.swal2-icon-show .swal2-success-line-tip{animation:swal2-toast-animate-success-line-tip .75s}.swal2-popup.swal2-toast .swal2-success.swal2-icon-show .swal2-success-line-long{animation:swal2-toast-animate-success-line-long .75s}.swal2-popup.swal2-toast.swal2-show{animation:swal2-toast-show .5s}.swal2-popup.swal2-toast.swal2-hide{animation:swal2-toast-hide .1s forwards}div:where(.swal2-container){display:grid;position:fixed;z-index:1060;inset:0;box-sizing:border-box;grid-template-areas:"top-start     top            top-end" "center-start  center         center-end" "bottom-start  bottom-center  bottom-end";grid-template-rows:minmax(min-content, auto) minmax(min-content, auto) minmax(min-content, auto);height:100%;padding:.625em;overflow-x:hidden;transition:background-color .1s;-webkit-overflow-scrolling:touch}div:where(.swal2-container).swal2-backdrop-show,div:where(.swal2-container).swal2-noanimation{background:rgba(0,0,0,.4)}div:where(.swal2-container).swal2-backdrop-hide{background:rgba(0,0,0,0) !important}div:where(.swal2-container).swal2-top-start,div:where(.swal2-container).swal2-center-start,div:where(.swal2-container).swal2-bottom-start{grid-template-columns:minmax(0, 1fr) auto auto}div:where(.swal2-container).swal2-top,div:where(.swal2-container).swal2-center,div:where(.swal2-container).swal2-bottom{grid-template-columns:auto minmax(0, 1fr) auto}div:where(.swal2-container).swal2-top-end,div:where(.swal2-container).swal2-center-end,div:where(.swal2-container).swal2-bottom-end{grid-template-columns:auto auto minmax(0, 1fr)}div:where(.swal2-container).swal2-top-start>.swal2-popup{align-self:start}div:where(.swal2-container).swal2-top>.swal2-popup{grid-column:2;align-self:start;justify-self:center}div:where(.swal2-container).swal2-top-end>.swal2-popup,div:where(.swal2-container).swal2-top-right>.swal2-popup{grid-column:3;align-self:start;justify-self:end}div:where(.swal2-container).swal2-center-start>.swal2-popup,div:where(.swal2-container).swal2-center-left>.swal2-popup{grid-row:2;align-self:center}div:where(.swal2-container).swal2-center>.swal2-popup{grid-column:2;grid-row:2;align-self:center;justify-self:center}div:where(.swal2-container).swal2-center-end>.swal2-popup,div:where(.swal2-container).swal2-center-right>.swal2-popup{grid-column:3;grid-row:2;align-self:center;justify-self:end}div:where(.swal2-container).swal2-bottom-start>.swal2-popup,div:where(.swal2-container).swal2-bottom-left>.swal2-popup{grid-column:1;grid-row:3;align-self:end}div:where(.swal2-container).swal2-bottom>.swal2-popup{grid-column:2;grid-row:3;justify-self:center;align-self:end}div:where(.swal2-container).swal2-bottom-end>.swal2-popup,div:where(.swal2-container).swal2-bottom-right>.swal2-popup{grid-column:3;grid-row:3;align-self:end;justify-self:end}div:where(.swal2-container).swal2-grow-row>.swal2-popup,div:where(.swal2-container).swal2-grow-fullscreen>.swal2-popup{grid-column:1/4;width:100%}div:where(.swal2-container).swal2-grow-column>.swal2-popup,div:where(.swal2-container).swal2-grow-fullscreen>.swal2-popup{grid-row:1/4;align-self:stretch}div:where(.swal2-container).swal2-no-transition{transition:none !important}div:where(.swal2-container) div:where(.swal2-popup){display:none;position:relative;box-sizing:border-box;grid-template-columns:minmax(0, 100%);width:32em;max-width:100%;padding:0 0 1.25em;border:none;border-radius:5px;background:#fff;color:#545454;font-family:inherit;font-size:1rem}div:where(.swal2-container) div:where(.swal2-popup):focus{outline:none}div:where(.swal2-container) div:where(.swal2-popup).swal2-loading{overflow-y:hidden}div:where(.swal2-container) h2:where(.swal2-title){position:relative;max-width:100%;margin:0;padding:.8em 1em 0;color:inherit;font-size:1.875em;font-weight:600;text-align:center;text-transform:none;word-wrap:break-word}div:where(.swal2-container) div:where(.swal2-actions){display:flex;z-index:1;box-sizing:border-box;flex-wrap:wrap;align-items:center;justify-content:center;width:auto;margin:1.25em auto 0;padding:0}div:where(.swal2-container) div:where(.swal2-actions):not(.swal2-loading) .swal2-styled[disabled]{opacity:.4}div:where(.swal2-container) div:where(.swal2-actions):not(.swal2-loading) .swal2-styled:hover{background-image:linear-gradient(rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.1))}div:where(.swal2-container) div:where(.swal2-actions):not(.swal2-loading) .swal2-styled:active{background-image:linear-gradient(rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2))}div:where(.swal2-container) div:where(.swal2-loader){display:none;align-items:center;justify-content:center;width:2.2em;height:2.2em;margin:0 1.875em;animation:swal2-rotate-loading 1.5s linear 0s infinite normal;border-width:.25em;border-style:solid;border-radius:100%;border-color:#2778c4 rgba(0,0,0,0) #2778c4 rgba(0,0,0,0)}div:where(.swal2-container) button:where(.swal2-styled){margin:.3125em;padding:.625em 1.1em;transition:box-shadow .1s;box-shadow:0 0 0 3px rgba(0,0,0,0);font-weight:500}div:where(.swal2-container) button:where(.swal2-styled):not([disabled]){cursor:pointer}div:where(.swal2-container) button:where(.swal2-styled).swal2-confirm{border:0;border-radius:.25em;background:initial;background-color:#7066e0;color:#fff;font-size:1em}div:where(.swal2-container) button:where(.swal2-styled).swal2-confirm:focus{box-shadow:0 0 0 3px rgba(112,102,224,.5)}div:where(.swal2-container) button:where(.swal2-styled).swal2-deny{border:0;border-radius:.25em;background:initial;background-color:#dc3741;color:#fff;font-size:1em}div:where(.swal2-container) button:where(.swal2-styled).swal2-deny:focus{box-shadow:0 0 0 3px rgba(220,55,65,.5)}div:where(.swal2-container) button:where(.swal2-styled).swal2-cancel{border:0;border-radius:.25em;background:initial;background-color:#6e7881;color:#fff;font-size:1em}div:where(.swal2-container) button:where(.swal2-styled).swal2-cancel:focus{box-shadow:0 0 0 3px rgba(110,120,129,.5)}div:where(.swal2-container) button:where(.swal2-styled).swal2-default-outline:focus{box-shadow:0 0 0 3px rgba(100,150,200,.5)}div:where(.swal2-container) button:where(.swal2-styled):focus{outline:none}div:where(.swal2-container) button:where(.swal2-styled)::-moz-focus-inner{border:0}div:where(.swal2-container) div:where(.swal2-footer){margin:1em 0 0;padding:1em 1em 0;border-top:1px solid #eee;color:inherit;font-size:1em;text-align:center}div:where(.swal2-container) .swal2-timer-progress-bar-container{position:absolute;right:0;bottom:0;left:0;grid-column:auto !important;overflow:hidden;border-bottom-right-radius:5px;border-bottom-left-radius:5px}div:where(.swal2-container) div:where(.swal2-timer-progress-bar){width:100%;height:.25em;background:rgba(0,0,0,.2)}div:where(.swal2-container) img:where(.swal2-image){max-width:100%;margin:2em auto 1em}div:where(.swal2-container) button:where(.swal2-close){z-index:2;align-items:center;justify-content:center;width:1.2em;height:1.2em;margin-top:0;margin-right:0;margin-bottom:-1.2em;padding:0;overflow:hidden;transition:color .1s,box-shadow .1s;border:none;border-radius:5px;background:rgba(0,0,0,0);color:#ccc;font-family:monospace;font-size:2.5em;cursor:pointer;justify-self:end}div:where(.swal2-container) button:where(.swal2-close):hover{transform:none;background:rgba(0,0,0,0);color:#f27474}div:where(.swal2-container) button:where(.swal2-close):focus{outline:none;box-shadow:inset 0 0 0 3px rgba(100,150,200,.5)}div:where(.swal2-container) button:where(.swal2-close)::-moz-focus-inner{border:0}div:where(.swal2-container) .swal2-html-container{z-index:1;justify-content:center;margin:1em 1.6em .3em;padding:0;overflow:auto;color:inherit;font-size:1.125em;font-weight:normal;line-height:normal;text-align:center;word-wrap:break-word;word-break:break-word}div:where(.swal2-container) input:where(.swal2-input),div:where(.swal2-container) input:where(.swal2-file),div:where(.swal2-container) textarea:where(.swal2-textarea),div:where(.swal2-container) select:where(.swal2-select),div:where(.swal2-container) div:where(.swal2-radio),div:where(.swal2-container) label:where(.swal2-checkbox){margin:1em 2em 3px}div:where(.swal2-container) input:where(.swal2-input),div:where(.swal2-container) input:where(.swal2-file),div:where(.swal2-container) textarea:where(.swal2-textarea){box-sizing:border-box;width:auto;transition:border-color .1s,box-shadow .1s;border:1px solid #d9d9d9;border-radius:.1875em;background:rgba(0,0,0,0);box-shadow:inset 0 1px 1px rgba(0,0,0,.06),0 0 0 3px rgba(0,0,0,0);color:inherit;font-size:1.125em}div:where(.swal2-container) input:where(.swal2-input).swal2-inputerror,div:where(.swal2-container) input:where(.swal2-file).swal2-inputerror,div:where(.swal2-container) textarea:where(.swal2-textarea).swal2-inputerror{border-color:#f27474 !important;box-shadow:0 0 2px #f27474 !important}div:where(.swal2-container) input:where(.swal2-input):focus,div:where(.swal2-container) input:where(.swal2-file):focus,div:where(.swal2-container) textarea:where(.swal2-textarea):focus{border:1px solid #b4dbed;outline:none;box-shadow:inset 0 1px 1px rgba(0,0,0,.06),0 0 0 3px rgba(100,150,200,.5)}div:where(.swal2-container) input:where(.swal2-input)::placeholder,div:where(.swal2-container) input:where(.swal2-file)::placeholder,div:where(.swal2-container) textarea:where(.swal2-textarea)::placeholder{color:#ccc}div:where(.swal2-container) .swal2-range{margin:1em 2em 3px;background:#fff}div:where(.swal2-container) .swal2-range input{width:80%}div:where(.swal2-container) .swal2-range output{width:20%;color:inherit;font-weight:600;text-align:center}div:where(.swal2-container) .swal2-range input,div:where(.swal2-container) .swal2-range output{height:2.625em;padding:0;font-size:1.125em;line-height:2.625em}div:where(.swal2-container) .swal2-input{height:2.625em;padding:0 .75em}div:where(.swal2-container) .swal2-file{width:75%;margin-right:auto;margin-left:auto;background:rgba(0,0,0,0);font-size:1.125em}div:where(.swal2-container) .swal2-textarea{height:6.75em;padding:.75em}div:where(.swal2-container) .swal2-select{min-width:50%;max-width:100%;padding:.375em .625em;background:rgba(0,0,0,0);color:inherit;font-size:1.125em}div:where(.swal2-container) .swal2-radio,div:where(.swal2-container) .swal2-checkbox{align-items:center;justify-content:center;background:#fff;color:inherit}div:where(.swal2-container) .swal2-radio label,div:where(.swal2-container) .swal2-checkbox label{margin:0 .6em;font-size:1.125em}div:where(.swal2-container) .swal2-radio input,div:where(.swal2-container) .swal2-checkbox input{flex-shrink:0;margin:0 .4em}div:where(.swal2-container) label:where(.swal2-input-label){display:flex;justify-content:center;margin:1em auto 0}div:where(.swal2-container) div:where(.swal2-validation-message){align-items:center;justify-content:center;margin:1em 0 0;padding:.625em;overflow:hidden;background:#f0f0f0;color:#666;font-size:1em;font-weight:300}div:where(.swal2-container) div:where(.swal2-validation-message)::before{content:"!";display:inline-block;width:1.5em;min-width:1.5em;height:1.5em;margin:0 .625em;border-radius:50%;background-color:#f27474;color:#fff;font-weight:600;line-height:1.5em;text-align:center}div:where(.swal2-container) .swal2-progress-steps{flex-wrap:wrap;align-items:center;max-width:100%;margin:1.25em auto;padding:0;background:rgba(0,0,0,0);font-weight:600}div:where(.swal2-container) .swal2-progress-steps li{display:inline-block;position:relative}div:where(.swal2-container) .swal2-progress-steps .swal2-progress-step{z-index:20;flex-shrink:0;width:2em;height:2em;border-radius:2em;background:#2778c4;color:#fff;line-height:2em;text-align:center}div:where(.swal2-container) .swal2-progress-steps .swal2-progress-step.swal2-active-progress-step{background:#2778c4}div:where(.swal2-container) .swal2-progress-steps .swal2-progress-step.swal2-active-progress-step~.swal2-progress-step{background:#add8e6;color:#fff}div:where(.swal2-container) .swal2-progress-steps .swal2-progress-step.swal2-active-progress-step~.swal2-progress-step-line{background:#add8e6}div:where(.swal2-container) .swal2-progress-steps .swal2-progress-step-line{z-index:10;flex-shrink:0;width:2.5em;height:.4em;margin:0 -1px;background:#2778c4}div:where(.swal2-icon){position:relative;box-sizing:content-box;justify-content:center;width:5em;height:5em;margin:2.5em auto .6em;border:0.25em solid rgba(0,0,0,0);border-radius:50%;border-color:#000;font-family:inherit;line-height:5em;cursor:default;user-select:none}div:where(.swal2-icon) .swal2-icon-content{display:flex;align-items:center;font-size:3.75em}div:where(.swal2-icon).swal2-error{border-color:#f27474;color:#f27474}div:where(.swal2-icon).swal2-error .swal2-x-mark{position:relative;flex-grow:1}div:where(.swal2-icon).swal2-error [class^=swal2-x-mark-line]{display:block;position:absolute;top:2.3125em;width:2.9375em;height:.3125em;border-radius:.125em;background-color:#f27474}div:where(.swal2-icon).swal2-error [class^=swal2-x-mark-line][class$=left]{left:1.0625em;transform:rotate(45deg)}div:where(.swal2-icon).swal2-error [class^=swal2-x-mark-line][class$=right]{right:1em;transform:rotate(-45deg)}div:where(.swal2-icon).swal2-error.swal2-icon-show{animation:swal2-animate-error-icon .5s}div:where(.swal2-icon).swal2-error.swal2-icon-show .swal2-x-mark{animation:swal2-animate-error-x-mark .5s}div:where(.swal2-icon).swal2-warning{border-color:#facea8;color:#f8bb86}div:where(.swal2-icon).swal2-warning.swal2-icon-show{animation:swal2-animate-error-icon .5s}div:where(.swal2-icon).swal2-warning.swal2-icon-show .swal2-icon-content{animation:swal2-animate-i-mark .5s}div:where(.swal2-icon).swal2-info{border-color:#9de0f6;color:#3fc3ee}div:where(.swal2-icon).swal2-info.swal2-icon-show{animation:swal2-animate-error-icon .5s}div:where(.swal2-icon).swal2-info.swal2-icon-show .swal2-icon-content{animation:swal2-animate-i-mark .8s}div:where(.swal2-icon).swal2-question{border-color:#c9dae1;color:#87adbd}div:where(.swal2-icon).swal2-question.swal2-icon-show{animation:swal2-animate-error-icon .5s}div:where(.swal2-icon).swal2-question.swal2-icon-show .swal2-icon-content{animation:swal2-animate-question-mark .8s}div:where(.swal2-icon).swal2-success{border-color:#a5dc86;color:#a5dc86}div:where(.swal2-icon).swal2-success [class^=swal2-success-circular-line]{position:absolute;width:3.75em;height:7.5em;transform:rotate(45deg);border-radius:50%}div:where(.swal2-icon).swal2-success [class^=swal2-success-circular-line][class$=left]{top:-0.4375em;left:-2.0635em;transform:rotate(-45deg);transform-origin:3.75em 3.75em;border-radius:7.5em 0 0 7.5em}div:where(.swal2-icon).swal2-success [class^=swal2-success-circular-line][class$=right]{top:-0.6875em;left:1.875em;transform:rotate(-45deg);transform-origin:0 3.75em;border-radius:0 7.5em 7.5em 0}div:where(.swal2-icon).swal2-success .swal2-success-ring{position:absolute;z-index:2;top:-0.25em;left:-0.25em;box-sizing:content-box;width:100%;height:100%;border:.25em solid rgba(165,220,134,.3);border-radius:50%}div:where(.swal2-icon).swal2-success .swal2-success-fix{position:absolute;z-index:1;top:.5em;left:1.625em;width:.4375em;height:5.625em;transform:rotate(-45deg)}div:where(.swal2-icon).swal2-success [class^=swal2-success-line]{display:block;position:absolute;z-index:2;height:.3125em;border-radius:.125em;background-color:#a5dc86}div:where(.swal2-icon).swal2-success [class^=swal2-success-line][class$=tip]{top:2.875em;left:.8125em;width:1.5625em;transform:rotate(45deg)}div:where(.swal2-icon).swal2-success [class^=swal2-success-line][class$=long]{top:2.375em;right:.5em;width:2.9375em;transform:rotate(-45deg)}div:where(.swal2-icon).swal2-success.swal2-icon-show .swal2-success-line-tip{animation:swal2-animate-success-line-tip .75s}div:where(.swal2-icon).swal2-success.swal2-icon-show .swal2-success-line-long{animation:swal2-animate-success-line-long .75s}div:where(.swal2-icon).swal2-success.swal2-icon-show .swal2-success-circular-line-right{animation:swal2-rotate-success-circular-line 4.25s ease-in}[class^=swal2]{-webkit-tap-highlight-color:rgba(0,0,0,0)}.swal2-show{animation:swal2-show .3s}.swal2-hide{animation:swal2-hide .15s forwards}.swal2-noanimation{transition:none}.swal2-scrollbar-measure{position:absolute;top:-9999px;width:50px;height:50px;overflow:scroll}.swal2-rtl .swal2-close{margin-right:initial;margin-left:0}.swal2-rtl .swal2-timer-progress-bar{right:0;left:auto}@keyframes swal2-toast-show{0%{transform:translateY(-0.625em) rotateZ(2deg)}33%{transform:translateY(0) rotateZ(-2deg)}66%{transform:translateY(0.3125em) rotateZ(2deg)}100%{transform:translateY(0) rotateZ(0deg)}}@keyframes swal2-toast-hide{100%{transform:rotateZ(1deg);opacity:0}}@keyframes swal2-toast-animate-success-line-tip{0%{top:.5625em;left:.0625em;width:0}54%{top:.125em;left:.125em;width:0}70%{top:.625em;left:-0.25em;width:1.625em}84%{top:1.0625em;left:.75em;width:.5em}100%{top:1.125em;left:.1875em;width:.75em}}@keyframes swal2-toast-animate-success-line-long{0%{top:1.625em;right:1.375em;width:0}65%{top:1.25em;right:.9375em;width:0}84%{top:.9375em;right:0;width:1.125em}100%{top:.9375em;right:.1875em;width:1.375em}}@keyframes swal2-show{0%{transform:scale(0.7)}45%{transform:scale(1.05)}80%{transform:scale(0.95)}100%{transform:scale(1)}}@keyframes swal2-hide{0%{transform:scale(1);opacity:1}100%{transform:scale(0.5);opacity:0}}@keyframes swal2-animate-success-line-tip{0%{top:1.1875em;left:.0625em;width:0}54%{top:1.0625em;left:.125em;width:0}70%{top:2.1875em;left:-0.375em;width:3.125em}84%{top:3em;left:1.3125em;width:1.0625em}100%{top:2.8125em;left:.8125em;width:1.5625em}}@keyframes swal2-animate-success-line-long{0%{top:3.375em;right:2.875em;width:0}65%{top:3.375em;right:2.875em;width:0}84%{top:2.1875em;right:0;width:3.4375em}100%{top:2.375em;right:.5em;width:2.9375em}}@keyframes swal2-rotate-success-circular-line{0%{transform:rotate(-45deg)}5%{transform:rotate(-45deg)}12%{transform:rotate(-405deg)}100%{transform:rotate(-405deg)}}@keyframes swal2-animate-error-x-mark{0%{margin-top:1.625em;transform:scale(0.4);opacity:0}50%{margin-top:1.625em;transform:scale(0.4);opacity:0}80%{margin-top:-0.375em;transform:scale(1.15)}100%{margin-top:0;transform:scale(1);opacity:1}}@keyframes swal2-animate-error-icon{0%{transform:rotateX(100deg);opacity:0}100%{transform:rotateX(0deg);opacity:1}}@keyframes swal2-rotate-loading{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@keyframes swal2-animate-question-mark{0%{transform:rotateY(-360deg)}100%{transform:rotateY(0)}}@keyframes swal2-animate-i-mark{0%{transform:rotateZ(45deg);opacity:0}25%{transform:rotateZ(-25deg);opacity:.4}50%{transform:rotateZ(15deg);opacity:.8}75%{transform:rotateZ(-5deg);opacity:1}100%{transform:rotateX(0);opacity:1}}body.swal2-shown:not(.swal2-no-backdrop):not(.swal2-toast-shown){overflow:hidden}body.swal2-height-auto{height:auto !important}body.swal2-no-backdrop .swal2-container{background-color:rgba(0,0,0,0) !important;pointer-events:none}body.swal2-no-backdrop .swal2-container .swal2-popup{pointer-events:all}body.swal2-no-backdrop .swal2-container .swal2-modal{box-shadow:0 0 10px rgba(0,0,0,.4)}@media print{body.swal2-shown:not(.swal2-no-backdrop):not(.swal2-toast-shown){overflow-y:scroll !important}body.swal2-shown:not(.swal2-no-backdrop):not(.swal2-toast-shown)>[aria-hidden=true]{display:none}body.swal2-shown:not(.swal2-no-backdrop):not(.swal2-toast-shown) .swal2-container{position:static !important}}body.swal2-toast-shown .swal2-container{box-sizing:border-box;width:360px;max-width:100%;background-color:rgba(0,0,0,0);pointer-events:none}body.swal2-toast-shown .swal2-container.swal2-top{inset:0 auto auto 50%;transform:translateX(-50%)}body.swal2-toast-shown .swal2-container.swal2-top-end,body.swal2-toast-shown .swal2-container.swal2-top-right{inset:0 0 auto auto}body.swal2-toast-shown .swal2-container.swal2-top-start,body.swal2-toast-shown .swal2-container.swal2-top-left{inset:0 auto auto 0}body.swal2-toast-shown .swal2-container.swal2-center-start,body.swal2-toast-shown .swal2-container.swal2-center-left{inset:50% auto auto 0;transform:translateY(-50%)}body.swal2-toast-shown .swal2-container.swal2-center{inset:50% auto auto 50%;transform:translate(-50%, -50%)}body.swal2-toast-shown .swal2-container.swal2-center-end,body.swal2-toast-shown .swal2-container.swal2-center-right{inset:50% 0 auto auto;transform:translateY(-50%)}body.swal2-toast-shown .swal2-container.swal2-bottom-start,body.swal2-toast-shown .swal2-container.swal2-bottom-left{inset:auto auto 0 0}body.swal2-toast-shown .swal2-container.swal2-bottom{inset:auto auto 0 50%;transform:translateX(-50%)}body.swal2-toast-shown .swal2-container.swal2-bottom-end,body.swal2-toast-shown .swal2-container.swal2-bottom-right{inset:auto 0 0 auto}</style><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script async="async" type="text/javascript" src="./4app_files/editor.main.js.download"></script><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./4app_files/editor.main.css"><script async="async" type="text/javascript" src="./4app_files/editor.main.nls.js.download"></script><script src="./4app_files/api.js.download" nonce=""></script><script src="./4app_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #383838; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #383838;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #383838;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #383838;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #383838;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #383838;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #383838; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./4app_files/gapi_loader.js.download" nonce=""></script><script src="./4app_files/socketio_binary.js.download" nonce=""></script><script src="./4app_files/analytics_binary.js.download" nonce=""></script><script src="./4app_files/MathJax.js.download" nonce=""></script><script src="./4app_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./4app_files/external_binary_l10n__en_gb.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$065098016$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$065098016$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$065098016$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$065098016$--><div class="mdc-snackbar__label" role="status" aria-live="polite">Loading…</div>
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_S" ng-non-bindable=""><div class="gb_Oc"><div>Google Account</div><div class="gb_g">Meshack Muthwii</div><div>meshmuth18@gmail.com</div><div class="gb_Pc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Gd;Gd=class extends _.pd{};_.Hd=function(a,b){if(b in a.i)return a.i[b];throw new Gd;};_.Id=function(a){return _.Hd(_.md.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Ld;_.Jd=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Ld=function(a){return new _.Kd(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Md=globalThis.trustedTypes;_.Nd=class{constructor(a){this.i=a}toString(){return this.i}};_.Od=new _.Nd("about:invalid#zClosurez");_.Kd=class{constructor(a){this.Th=a}};_.Pd=[Ld("data"),Ld("http"),Ld("https"),Ld("mailto"),Ld("ftp"),new _.Kd(a=>/^[^:]*([/?#]|$)/.test(a))];_.Qd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Rd=new _.Qd(_.Md?_.Md.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Vd,fe,ie,Ud,Wd,ae;_.Sd=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.Td=function(a,b){return a.lastIndexOf(b,0)==0};Vd=function(){let a=null;if(!Ud)return a;try{const b=c=>c;a=Ud.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Xd=function(){Wd===void 0&&(Wd=Vd());return Wd};_.Zd=function(a){const b=_.Xd();a=b?b.createScriptURL(a):a;return new _.Yd(a)};
_.$d=function(a){if(a instanceof _.Yd)return a.i;throw Error("x");};_.be=function(a){if(ae.test(a))return a};_.ce=function(a){if(a instanceof _.Nd)if(a instanceof _.Nd)a=a.i;else throw Error("x");else a=_.be(a);return a};_.de=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.S=function(a,b,c){return _.Ma(_.Lc(a,b,c,_.Kc))};_.ee=function(a,b){return _.Sd(_.Lc(a,b,void 0,_.Kc))};
fe=class extends _.O{constructor(a){super(a)}Wb(a){return _.L(this,24,a)}};_.ge=function(){return _.C(_.hd,fe,1)};_.he=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};Ud=_.Md;_.Yd=class{constructor(a){this.i=a}toString(){return this.i+""}};ae=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var oe,se,je;_.le=function(a){return a?new je(_.ke(a)):ie||(ie=new je)};_.me=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.T=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.ne(c,"*",a,b)[0]||null);return a||null};_.ne=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.pe=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:oe.hasOwnProperty(d)?a.setAttribute(oe[d],c):_.Td(d,"aria-")||_.Td(d,"data-")?a.setAttribute(d,c):a[d]=c})};oe={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.qe=function(a){return a?a.defaultView:window};_.te=function(a,b){const c=b[1],d=_.re(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.pe(d,c));b.length>2&&se(a,d,b);return d};se=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.he(f)||_.Lb(f)&&f.nodeType>0?d(f):_.bc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Jd(f):f,d)}};
_.ue=function(a){return _.re(document,a)};_.re=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ve=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.we=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.xe=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ke=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};je=function(a){this.i=a||_.t.document||document};_.n=je.prototype;
_.n.H=function(a){return _.me(this.i,a)};_.n.Pa=function(a,b,c){return _.te(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Je=_.ve;_.n.ng=_.we;_.n.mg=_.xe;
}catch(e){_._DumpException(e)}
try{
_.Mi=function(a){const b=_.de("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Ni=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.Zd(a);return b};_.Oi=function(a,b,c){a=a.fa;return _.zb(a,a[_.v]|0,b,c)!==void 0};_.Pi=class extends _.O{constructor(a){super(a)}};_.Qi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Si=function(a,b,c){a<b?Ri(a+1,b):_.Xc.log(Error("W`"+a+"`"+b),{url:c})},Ri=function(a,b){if(Ti){const c=_.ue("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.$d(Ti);_.Mi(c);c.onerror=_.Ob(Si,a,b,c.src);_.Qi("HEAD")[0].appendChild(c)}},Ui=class extends _.O{constructor(a){super(a)}};var Vi=_.C(_.hd,Ui,17)||new Ui,Wi,Ti=(Wi=_.C(Vi,_.Pi,1))?_.Ni(Wi):null,Xi,Yi=(Xi=_.C(Vi,_.Pi,2))?_.Ni(Xi):null,Zi=function(){Ri(1,2);if(Yi){const a=_.ue("LINK");a.setAttribute("type","text/css");a.href=_.$d(Yi).toString();a.rel="stylesheet";let b=_.de("style",document);b&&a.setAttribute("nonce",b);_.Qi("HEAD")[0].appendChild(a)}};(function(){const a=_.ge();if(_.S(a,18))Zi();else{const b=_.ee(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Zi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./4app_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$065098016$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><a id="link" class="button" href="https://colab.research.google.com/drive/1u-ewO-2_H37_lNGG7F81YmKRR4zkwmlR#notebook-main"><!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </a>
    </template><!--?lit$065098016$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$065098016$-->
    <!--?lit$065098016$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning"><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$065098016$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1u-ewO-2_H37_lNGG7F81YmKRR4zkwmlR#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$065098016$--> <!--?lit$065098016$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><div id="header-logo">
              <!--?lit$065098016$--> <!--?lit$065098016$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$065098016$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$--><svg viewBox="0 0 24 24"><!--?lit$065098016$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$065098016$--> <!--?lit$065098016$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 62.5781px;"><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">app.py_</colab-input-sizer>
            <!--?lit$065098016$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" value="" class="starred" data-aria-label="Unstar"><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Unstar">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Unstar notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$065098016$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$065098016$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$065098016$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$065098016$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$065098016$-->
      <!--?lit$065098016$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$065098016$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$065098016$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$065098016$--> <md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->people</md-icon>
                <!--?lit$065098016$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$065098016$--> <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$065098016$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Fa gb_Bd gb_ub gb_bd gb_H" id="gb" style="background-color: transparent;"><div class="gb_0d gb_rb gb_Qd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Ad" style="display:block"><div class="gb_hd"></div><div class="gb_z gb_td gb_Pf gb_0"><div class="gb_D gb_qb gb_Pf gb_0"><a class="gb_B gb_Za gb_0" aria-expanded="false" aria-label="Google Account: Meshack Muthwii  
(meshmuth18@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en-GB&amp;continue=https://colab.research.google.com/&amp;ec=GBRAqQM" tabindex="0" role="button"><span class="gb_ae"><img class="gb_P gbii" src="./4app_files/unnamed.jpg" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyjKN5b2lXUDZtPwIVdkl0cEPWuZ-ldDD_buguxlwMk0f4Q=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyjKN5b2lXUDZtPwIVdkl0cEPWuZ-ldDD_buguxlwMk0f4Q=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_Q gb_R" aria-hidden="true"><svg class="gb_Ka" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_La" cx="7" cy="7" r="7"></circle><path class="gb_Na" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Cd=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Cd(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Dd=document.querySelector(".gb_J .gb_B"),Ed=document.querySelector("#gb.gb_7c");Dd&&!Ed&&_.Cd(_.ld,Dd,"click");
}catch(e){_._DumpException(e)}
try{
_.mh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ha()&&a.i[b].B())return a.i[b];return null};_.nh=function(a,b){a.i[b.J()]=b};var oh=new class extends _.P{constructor(){var a=_.Xc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.mh(this)&&_.mh(this).J()==a||this.i[a].P(!0))}Ra(a){this.j=a;for(const b in this.i)this.i[b].ha()&&this.i[b].Ra(a)}kc(a){return a in this.i?this.i[a]:null}};_.od("dd",oh);
}catch(e){_._DumpException(e)}
try{
_.Fi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Gi=document.querySelector(".gb_z .gb_B"),Hi=document.querySelector("#gb.gb_7c");Gi&&!Hi&&_.Cd(_.ld,Gi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$065098016$-->
    <!--?lit$065098016$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <!--?lit$065098016$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$065098016$--><span class="screenreader-only"><!--?lit$065098016$-->Show command palette <!--?lit$065098016$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$065098016$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$065098016$-->Commands
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$065098016$--><span class="toolbar-add-code-split"><colab-toolbar-button class="split-button" command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <!--?lit$065098016$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$065098016$--><span class="screenreader-only"><!--?lit$065098016$-->Insert code cell below <!--?lit$065098016$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$065098016$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
              <!--?lit$065098016$-->Code
            </colab-toolbar-button>
            <!--?lit$065098016$--></span>
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <!--?lit$065098016$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$065098016$--><span class="screenreader-only"><!--?lit$065098016$-->Add text cell <!--?lit$065098016$--></span>
      </md-text-button>
      <!--?lit$065098016$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$065098016$-->Text
          </colab-toolbar-button>
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button class="split-button" icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <!--?lit$065098016$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$065098016$--><span class="screenreader-only"><!--?lit$065098016$-->Run all cells in notebook <!--?lit$065098016$--></span>
      </md-text-button>
      <!--?lit$065098016$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$065098016$-->Run all
      </colab-toolbar-button>
      <!--?lit$065098016$--><md-icon-button data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$065098016$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$065098016$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$065098016$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$065098016$--><!----><md-menu-item command="restart" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$065098016$-->
    <!--?lit$065098016$-->
    <!--?lit$065098016$-->
    <!--?lit$065098016$-->
    <!--?lit$065098016$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><md-icon-button id="button" data-aria-label="All changes saved" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="All changes saved">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->cloud_done</md-icon></md-icon-button><colab-tooltip-trigger aria-hidden="true" for="button" id="button-tooltip" message="All changes saved"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->All changes saved</div><!----><!--?--></template>
        </colab-tooltip-trigger></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>
    <!--?lit$065098016$-->
    <!--?lit$065098016$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$065098016$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$065098016$--><!--?lit$065098016$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$065098016$--> <!--?lit$065098016$--><!--?-->
      <colab-toolbar-button id="connect" class="split-button" tooltipid="colab-connect-tooltip" tooltiptext="Connect to a new runtime"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <!--?lit$065098016$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$065098016$--><span class="screenreader-only"><!--?lit$065098016$-->Connect to a new runtime <!--?lit$065098016$--></span>
      </md-text-button>
      <!--?lit$065098016$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connect to a new runtime" shortcut=""><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Connect to a new runtime</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$065098016$-->Connect
      </colab-toolbar-button>
      <!--?lit$065098016$--> <md-icon-button id="connect-dropdown" class="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$065098016$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$065098016$-->
    <span class="collapsed-options">
      <!--?lit$065098016$--><span class="colab-separator"></span>
      <!--?lit$065098016$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$065098016$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$065098016$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$065098016$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$065098016$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$065098016$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$065098016$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$065098016$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$065098016$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->code</md-icon>
    </md-icon-button> <!--?lit$065098016$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$065098016$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$065098016$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$065098016$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->folder</md-icon>
    </md-icon-button> <!--?lit$065098016$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$065098016$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$065098016$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-XNnnUflkDsA0" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$065098016$--><div class="indicator"></div>
      </div>
      <!--?lit$065098016$-->
    </div></template>
          <div class="colab-tab-header"> <!--?lit$065098016$--><span class="colab-tab-title" id="tab-title-XNnnUflkDsA0">
          <!--?lit$065098016$--><!--?lit$065098016$-->Notebook<!--?-->
        </span> <!--?lit$065098016$--> </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$065098016$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-0-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-0-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$065098016$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$065098016$-->
              <div class="notebook-content ">
                <!--?lit$065098016$--><div class="add-cell">
      <hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code notebook-cell cell-ui-refresh focused" id="cell-3q2spFLvDsAD" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$065098016$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->arrow_upward</md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Move cell up</div><!----><!----><div><!--?lit$065098016$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" aria-disabled="true">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->arrow_downward</md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Move cell down</div><!----><!----><div><!--?lit$065098016$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$065098016$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-3q2spFLvDsAD" anchor="ai-menu-anchor-3q2spFLvDsAD" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$065098016$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$065098016$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$065098016$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$065098016$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-3q2spFLvDsAD-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-3q2spFLvDsAD" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>
              <!--?lit$065098016$-->spark
            </md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-3q2spFLvDsAD" id="ai-menu-anchor-3q2spFLvDsAD-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->link</md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->comment</md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Add a comment</div><!----><!----><div><!--?lit$065098016$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->settings</md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->edit</md-icon>
        <!--?lit$065098016$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$--><svg viewBox="0 0 24 24"><!--?lit$065098016$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->delete</md-icon>
        <!--?lit$065098016$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Delete cell</div><!----><!----><div><!--?lit$065098016$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$065098016$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button class="cell-ui-refresh"><template shadowrootmode="open"><!----> <div class="cell-execution focused stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$065098016$-->
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$065098016$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$065098016$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$065098016$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$065098016$-->cell has not been executed in this session</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$065098016$--><div class="status">
      <div class="execution-count"><!--?lit$065098016$-->[ ]</div>
      <!--?lit$065098016$-->
    </div>
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 3345px; --vscode-editorCodeLens-lineHeight: 20px; --vscode-editorCodeLens-fontSize: 16px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/3" style="width: 1205px; height: 3345px;"><div data-mprt="3" class="overflow-guard" style="width: 1205px; height: 3345px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 3345px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 3345px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 18px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 23px; letter-spacing: 0px; width: 6px; height: 3345px;"><div style="position:absolute;top:0px;width:100%;height:23px;"></div><div style="position:absolute;top:23px;width:100%;height:23px;"></div><div style="position:absolute;top:46px;width:100%;height:23px;"></div><div style="position:absolute;top:69px;width:100%;height:23px;"></div><div style="position:absolute;top:92px;width:100%;height:23px;"></div><div style="position:absolute;top:115px;width:100%;height:23px;"></div><div style="position:absolute;top:138px;width:100%;height:23px;"></div><div style="position:absolute;top:161px;width:100%;height:23px;"></div><div style="position:absolute;top:184px;width:100%;height:23px;"></div><div style="position:absolute;top:207px;width:100%;height:23px;"></div><div style="position:absolute;top:230px;width:100%;height:23px;"></div><div style="position:absolute;top:253px;width:100%;height:23px;"></div><div style="position:absolute;top:276px;width:100%;height:23px;"></div><div style="position:absolute;top:299px;width:100%;height:23px;"></div><div style="position:absolute;top:322px;width:100%;height:23px;"></div><div style="position:absolute;top:345px;width:100%;height:23px;"></div><div style="position:absolute;top:368px;width:100%;height:23px;"></div><div style="position:absolute;top:391px;width:100%;height:23px;"></div><div style="position:absolute;top:414px;width:100%;height:23px;"></div><div style="position:absolute;top:437px;width:100%;height:23px;"></div><div style="position:absolute;top:460px;width:100%;height:23px;"></div><div style="position:absolute;top:483px;width:100%;height:23px;"></div><div style="position:absolute;top:506px;width:100%;height:23px;"></div><div style="position:absolute;top:529px;width:100%;height:23px;"></div><div style="position:absolute;top:552px;width:100%;height:23px;"></div><div style="position:absolute;top:575px;width:100%;height:23px;"></div><div style="position:absolute;top:598px;width:100%;height:23px;"></div><div style="position:absolute;top:621px;width:100%;height:23px;"></div><div style="position:absolute;top:644px;width:100%;height:23px;"></div><div style="position:absolute;top:667px;width:100%;height:23px;"></div><div style="position:absolute;top:690px;width:100%;height:23px;"></div><div style="position:absolute;top:713px;width:100%;height:23px;"></div><div style="position:absolute;top:736px;width:100%;height:23px;"></div><div style="position:absolute;top:759px;width:100%;height:23px;"></div><div style="position:absolute;top:782px;width:100%;height:23px;"></div><div style="position:absolute;top:805px;width:100%;height:23px;"></div><div style="position:absolute;top:828px;width:100%;height:23px;"></div><div style="position:absolute;top:851px;width:100%;height:23px;"></div><div style="position:absolute;top:874px;width:100%;height:23px;"></div><div style="position:absolute;top:897px;width:100%;height:23px;"></div><div style="position:absolute;top:920px;width:100%;height:23px;"></div><div style="position:absolute;top:943px;width:100%;height:23px;"></div><div style="position:absolute;top:966px;width:100%;height:23px;"></div><div style="position:absolute;top:989px;width:100%;height:23px;"></div><div style="position:absolute;top:1012px;width:100%;height:23px;"></div><div style="position:absolute;top:1035px;width:100%;height:23px;"></div><div style="position:absolute;top:1058px;width:100%;height:23px;"></div><div style="position:absolute;top:1081px;width:100%;height:23px;"></div><div style="position:absolute;top:1104px;width:100%;height:23px;"></div><div style="position:absolute;top:1127px;width:100%;height:23px;"></div><div style="position:absolute;top:1150px;width:100%;height:23px;"></div><div style="position:absolute;top:1173px;width:100%;height:23px;"></div><div style="position:absolute;top:1196px;width:100%;height:23px;"></div><div style="position:absolute;top:1219px;width:100%;height:23px;"></div><div style="position:absolute;top:1242px;width:100%;height:23px;"></div><div style="position:absolute;top:1265px;width:100%;height:23px;"></div><div style="position:absolute;top:1288px;width:100%;height:23px;"></div><div style="position:absolute;top:1311px;width:100%;height:23px;"></div><div style="position:absolute;top:1334px;width:100%;height:23px;"></div><div style="position:absolute;top:1357px;width:100%;height:23px;"></div><div style="position:absolute;top:1380px;width:100%;height:23px;"></div><div style="position:absolute;top:1403px;width:100%;height:23px;"></div><div style="position:absolute;top:1426px;width:100%;height:23px;"></div><div style="position:absolute;top:1449px;width:100%;height:23px;"></div><div style="position:absolute;top:1472px;width:100%;height:23px;"></div><div style="position:absolute;top:1495px;width:100%;height:23px;"></div><div style="position:absolute;top:1518px;width:100%;height:23px;"></div><div style="position:absolute;top:1541px;width:100%;height:23px;"></div><div style="position:absolute;top:1564px;width:100%;height:23px;"></div><div style="position:absolute;top:1587px;width:100%;height:23px;"></div><div style="position:absolute;top:1610px;width:100%;height:23px;"></div><div style="position:absolute;top:1633px;width:100%;height:23px;"></div><div style="position:absolute;top:1656px;width:100%;height:23px;"></div><div style="position:absolute;top:1679px;width:100%;height:23px;"></div><div style="position:absolute;top:1702px;width:100%;height:23px;"></div><div style="position:absolute;top:1725px;width:100%;height:23px;"></div><div style="position:absolute;top:1748px;width:100%;height:23px;"></div><div style="position:absolute;top:1771px;width:100%;height:23px;"></div><div style="position:absolute;top:1794px;width:100%;height:23px;"></div><div style="position:absolute;top:1817px;width:100%;height:23px;"></div><div style="position:absolute;top:1840px;width:100%;height:23px;"></div><div style="position:absolute;top:1863px;width:100%;height:23px;"></div><div style="position:absolute;top:1886px;width:100%;height:23px;"></div><div style="position:absolute;top:1909px;width:100%;height:23px;"></div><div style="position:absolute;top:1932px;width:100%;height:23px;"></div><div style="position:absolute;top:1955px;width:100%;height:23px;"></div><div style="position:absolute;top:1978px;width:100%;height:23px;"></div><div style="position:absolute;top:2001px;width:100%;height:23px;"></div><div style="position:absolute;top:2024px;width:100%;height:23px;"></div><div style="position:absolute;top:2047px;width:100%;height:23px;"></div><div style="position:absolute;top:2070px;width:100%;height:23px;"></div><div style="position:absolute;top:2093px;width:100%;height:23px;"></div><div style="position:absolute;top:2116px;width:100%;height:23px;"></div><div style="position:absolute;top:2139px;width:100%;height:23px;"></div><div style="position:absolute;top:2162px;width:100%;height:23px;"></div><div style="position:absolute;top:2185px;width:100%;height:23px;"></div><div style="position:absolute;top:2208px;width:100%;height:23px;"></div><div style="position:absolute;top:2231px;width:100%;height:23px;"></div><div style="position:absolute;top:2254px;width:100%;height:23px;"></div><div style="position:absolute;top:2277px;width:100%;height:23px;"></div><div style="position:absolute;top:2300px;width:100%;height:23px;"></div><div style="position:absolute;top:2323px;width:100%;height:23px;"></div><div style="position:absolute;top:2346px;width:100%;height:23px;"></div><div style="position:absolute;top:2369px;width:100%;height:23px;"></div><div style="position:absolute;top:2392px;width:100%;height:23px;"></div><div style="position:absolute;top:2415px;width:100%;height:23px;"></div><div style="position:absolute;top:2438px;width:100%;height:23px;"></div><div style="position:absolute;top:2461px;width:100%;height:23px;"></div><div style="position:absolute;top:2484px;width:100%;height:23px;"></div><div style="position:absolute;top:2507px;width:100%;height:23px;"></div><div style="position:absolute;top:2530px;width:100%;height:23px;"></div><div style="position:absolute;top:2553px;width:100%;height:23px;"></div><div style="position:absolute;top:2576px;width:100%;height:23px;"></div><div style="position:absolute;top:2599px;width:100%;height:23px;"></div><div style="position:absolute;top:2622px;width:100%;height:23px;"></div><div style="position:absolute;top:2645px;width:100%;height:23px;"></div><div style="position:absolute;top:2668px;width:100%;height:23px;"></div><div style="position:absolute;top:2691px;width:100%;height:23px;"></div><div style="position:absolute;top:2714px;width:100%;height:23px;"></div><div style="position:absolute;top:2737px;width:100%;height:23px;"></div><div style="position:absolute;top:2760px;width:100%;height:23px;"></div><div style="position:absolute;top:2783px;width:100%;height:23px;"></div><div style="position:absolute;top:2806px;width:100%;height:23px;"></div><div style="position:absolute;top:2829px;width:100%;height:23px;"></div><div style="position:absolute;top:2852px;width:100%;height:23px;"></div><div style="position:absolute;top:2875px;width:100%;height:23px;"></div><div style="position:absolute;top:2898px;width:100%;height:23px;"></div><div style="position:absolute;top:2921px;width:100%;height:23px;"></div><div style="position:absolute;top:2944px;width:100%;height:23px;"></div><div style="position:absolute;top:2967px;width:100%;height:23px;"></div><div style="position:absolute;top:2990px;width:100%;height:23px;"></div><div style="position:absolute;top:3013px;width:100%;height:23px;"></div><div style="position:absolute;top:3036px;width:100%;height:23px;"></div><div style="position:absolute;top:3059px;width:100%;height:23px;"></div><div style="position:absolute;top:3082px;width:100%;height:23px;"></div><div style="position:absolute;top:3105px;width:100%;height:23px;"></div><div style="position:absolute;top:3128px;width:100%;height:23px;"></div><div style="position:absolute;top:3151px;width:100%;height:23px;"></div><div style="position:absolute;top:3174px;width:100%;height:23px;"></div><div style="position:absolute;top:3197px;width:100%;height:23px;"></div><div style="position:absolute;top:3220px;width:100%;height:23px;"></div><div style="position:absolute;top:3243px;width:100%;height:23px;"></div><div style="position:absolute;top:3266px;width:100%;height:23px;"></div><div style="position:absolute;top:3289px;width:100%;height:23px;"></div><div style="position:absolute;top:3312px;width:100%;height:23px;"><div class="current-line current-line-margin-both" style="width:6px; height:23px;"></div></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1199px; height: 3345px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 3345px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 18px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 23px; letter-spacing: 0px; height: 0px; width: 1894px;"><div style="position:absolute;top:0px;width:100%;height:23px;"></div><div style="position:absolute;top:23px;width:100%;height:23px;"></div><div style="position:absolute;top:46px;width:100%;height:23px;"></div><div style="position:absolute;top:69px;width:100%;height:23px;"></div><div style="position:absolute;top:92px;width:100%;height:23px;"></div><div style="position:absolute;top:115px;width:100%;height:23px;"></div><div style="position:absolute;top:138px;width:100%;height:23px;"></div><div style="position:absolute;top:161px;width:100%;height:23px;"></div><div style="position:absolute;top:184px;width:100%;height:23px;"></div><div style="position:absolute;top:207px;width:100%;height:23px;"></div><div style="position:absolute;top:230px;width:100%;height:23px;"></div><div style="position:absolute;top:253px;width:100%;height:23px;"></div><div style="position:absolute;top:276px;width:100%;height:23px;"></div><div style="position:absolute;top:299px;width:100%;height:23px;"></div><div style="position:absolute;top:322px;width:100%;height:23px;"></div><div style="position:absolute;top:345px;width:100%;height:23px;"></div><div style="position:absolute;top:368px;width:100%;height:23px;"></div><div style="position:absolute;top:391px;width:100%;height:23px;"></div><div style="position:absolute;top:414px;width:100%;height:23px;"></div><div style="position:absolute;top:437px;width:100%;height:23px;"></div><div style="position:absolute;top:460px;width:100%;height:23px;"></div><div style="position:absolute;top:483px;width:100%;height:23px;"></div><div style="position:absolute;top:506px;width:100%;height:23px;"></div><div style="position:absolute;top:529px;width:100%;height:23px;"></div><div style="position:absolute;top:552px;width:100%;height:23px;"></div><div style="position:absolute;top:575px;width:100%;height:23px;"></div><div style="position:absolute;top:598px;width:100%;height:23px;"></div><div style="position:absolute;top:621px;width:100%;height:23px;"></div><div style="position:absolute;top:644px;width:100%;height:23px;"></div><div style="position:absolute;top:667px;width:100%;height:23px;"></div><div style="position:absolute;top:690px;width:100%;height:23px;"></div><div style="position:absolute;top:713px;width:100%;height:23px;"></div><div style="position:absolute;top:736px;width:100%;height:23px;"></div><div style="position:absolute;top:759px;width:100%;height:23px;"></div><div style="position:absolute;top:782px;width:100%;height:23px;"></div><div style="position:absolute;top:805px;width:100%;height:23px;"></div><div style="position:absolute;top:828px;width:100%;height:23px;"></div><div style="position:absolute;top:851px;width:100%;height:23px;"></div><div style="position:absolute;top:874px;width:100%;height:23px;"></div><div style="position:absolute;top:897px;width:100%;height:23px;"></div><div style="position:absolute;top:920px;width:100%;height:23px;"></div><div style="position:absolute;top:943px;width:100%;height:23px;"></div><div style="position:absolute;top:966px;width:100%;height:23px;"></div><div style="position:absolute;top:989px;width:100%;height:23px;"></div><div style="position:absolute;top:1012px;width:100%;height:23px;"></div><div style="position:absolute;top:1035px;width:100%;height:23px;"></div><div style="position:absolute;top:1058px;width:100%;height:23px;"></div><div style="position:absolute;top:1081px;width:100%;height:23px;"></div><div style="position:absolute;top:1104px;width:100%;height:23px;"></div><div style="position:absolute;top:1127px;width:100%;height:23px;"></div><div style="position:absolute;top:1150px;width:100%;height:23px;"></div><div style="position:absolute;top:1173px;width:100%;height:23px;"></div><div style="position:absolute;top:1196px;width:100%;height:23px;"></div><div style="position:absolute;top:1219px;width:100%;height:23px;"></div><div style="position:absolute;top:1242px;width:100%;height:23px;"></div><div style="position:absolute;top:1265px;width:100%;height:23px;"></div><div style="position:absolute;top:1288px;width:100%;height:23px;"></div><div style="position:absolute;top:1311px;width:100%;height:23px;"></div><div style="position:absolute;top:1334px;width:100%;height:23px;"></div><div style="position:absolute;top:1357px;width:100%;height:23px;"></div><div style="position:absolute;top:1380px;width:100%;height:23px;"></div><div style="position:absolute;top:1403px;width:100%;height:23px;"></div><div style="position:absolute;top:1426px;width:100%;height:23px;"></div><div style="position:absolute;top:1449px;width:100%;height:23px;"></div><div style="position:absolute;top:1472px;width:100%;height:23px;"></div><div style="position:absolute;top:1495px;width:100%;height:23px;"></div><div style="position:absolute;top:1518px;width:100%;height:23px;"></div><div style="position:absolute;top:1541px;width:100%;height:23px;"></div><div style="position:absolute;top:1564px;width:100%;height:23px;"></div><div style="position:absolute;top:1587px;width:100%;height:23px;"></div><div style="position:absolute;top:1610px;width:100%;height:23px;"></div><div style="position:absolute;top:1633px;width:100%;height:23px;"></div><div style="position:absolute;top:1656px;width:100%;height:23px;"></div><div style="position:absolute;top:1679px;width:100%;height:23px;"></div><div style="position:absolute;top:1702px;width:100%;height:23px;"></div><div style="position:absolute;top:1725px;width:100%;height:23px;"></div><div style="position:absolute;top:1748px;width:100%;height:23px;"></div><div style="position:absolute;top:1771px;width:100%;height:23px;"></div><div style="position:absolute;top:1794px;width:100%;height:23px;"></div><div style="position:absolute;top:1817px;width:100%;height:23px;"></div><div style="position:absolute;top:1840px;width:100%;height:23px;"></div><div style="position:absolute;top:1863px;width:100%;height:23px;"></div><div style="position:absolute;top:1886px;width:100%;height:23px;"></div><div style="position:absolute;top:1909px;width:100%;height:23px;"></div><div style="position:absolute;top:1932px;width:100%;height:23px;"></div><div style="position:absolute;top:1955px;width:100%;height:23px;"></div><div style="position:absolute;top:1978px;width:100%;height:23px;"></div><div style="position:absolute;top:2001px;width:100%;height:23px;"></div><div style="position:absolute;top:2024px;width:100%;height:23px;"></div><div style="position:absolute;top:2047px;width:100%;height:23px;"></div><div style="position:absolute;top:2070px;width:100%;height:23px;"></div><div style="position:absolute;top:2093px;width:100%;height:23px;"></div><div style="position:absolute;top:2116px;width:100%;height:23px;"></div><div style="position:absolute;top:2139px;width:100%;height:23px;"></div><div style="position:absolute;top:2162px;width:100%;height:23px;"></div><div style="position:absolute;top:2185px;width:100%;height:23px;"></div><div style="position:absolute;top:2208px;width:100%;height:23px;"></div><div style="position:absolute;top:2231px;width:100%;height:23px;"></div><div style="position:absolute;top:2254px;width:100%;height:23px;"></div><div style="position:absolute;top:2277px;width:100%;height:23px;"></div><div style="position:absolute;top:2300px;width:100%;height:23px;"></div><div style="position:absolute;top:2323px;width:100%;height:23px;"></div><div style="position:absolute;top:2346px;width:100%;height:23px;"></div><div style="position:absolute;top:2369px;width:100%;height:23px;"></div><div style="position:absolute;top:2392px;width:100%;height:23px;"></div><div style="position:absolute;top:2415px;width:100%;height:23px;"></div><div style="position:absolute;top:2438px;width:100%;height:23px;"></div><div style="position:absolute;top:2461px;width:100%;height:23px;"></div><div style="position:absolute;top:2484px;width:100%;height:23px;"></div><div style="position:absolute;top:2507px;width:100%;height:23px;"></div><div style="position:absolute;top:2530px;width:100%;height:23px;"></div><div style="position:absolute;top:2553px;width:100%;height:23px;"></div><div style="position:absolute;top:2576px;width:100%;height:23px;"></div><div style="position:absolute;top:2599px;width:100%;height:23px;"></div><div style="position:absolute;top:2622px;width:100%;height:23px;"></div><div style="position:absolute;top:2645px;width:100%;height:23px;"></div><div style="position:absolute;top:2668px;width:100%;height:23px;"></div><div style="position:absolute;top:2691px;width:100%;height:23px;"></div><div style="position:absolute;top:2714px;width:100%;height:23px;"></div><div style="position:absolute;top:2737px;width:100%;height:23px;"></div><div style="position:absolute;top:2760px;width:100%;height:23px;"></div><div style="position:absolute;top:2783px;width:100%;height:23px;"></div><div style="position:absolute;top:2806px;width:100%;height:23px;"></div><div style="position:absolute;top:2829px;width:100%;height:23px;"></div><div style="position:absolute;top:2852px;width:100%;height:23px;"></div><div style="position:absolute;top:2875px;width:100%;height:23px;"></div><div style="position:absolute;top:2898px;width:100%;height:23px;"></div><div style="position:absolute;top:2921px;width:100%;height:23px;"></div><div style="position:absolute;top:2944px;width:100%;height:23px;"></div><div style="position:absolute;top:2967px;width:100%;height:23px;"></div><div style="position:absolute;top:2990px;width:100%;height:23px;"></div><div style="position:absolute;top:3013px;width:100%;height:23px;"></div><div style="position:absolute;top:3036px;width:100%;height:23px;"></div><div style="position:absolute;top:3059px;width:100%;height:23px;"></div><div style="position:absolute;top:3082px;width:100%;height:23px;"></div><div style="position:absolute;top:3105px;width:100%;height:23px;"></div><div style="position:absolute;top:3128px;width:100%;height:23px;"></div><div style="position:absolute;top:3151px;width:100%;height:23px;"></div><div style="position:absolute;top:3174px;width:100%;height:23px;"></div><div style="position:absolute;top:3197px;width:100%;height:23px;"></div><div style="position:absolute;top:3220px;width:100%;height:23px;"></div><div style="position:absolute;top:3243px;width:100%;height:23px;"></div><div style="position:absolute;top:3266px;width:100%;height:23px;"></div><div style="position:absolute;top:3289px;width:100%;height:23px;"></div><div style="position:absolute;top:3312px;width:100%;height:23px;"><div class="current-line" style="width:1894px; height:23px;"></div></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 4px; height: 3345px; left: 791.875px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 18px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 23px; letter-spacing: 0px; width: 1894px; height: 3345px;"><div style="top:0px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;app.py</span></span></div><div style="top:23px;height:23px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;streamlit&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;st</span></span></div><div style="top:46px;height:23px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;pandas&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;pd</span></span></div><div style="top:69px;height:23px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;smtplib</span></span></div><div style="top:92px;height:23px;" class="view-line"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;email.mime.text&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;MIMEText</span></span></div><div style="top:115px;height:23px;" class="view-line"><span><span class="mtk20">from</span><span class="mtk1">&nbsp;datetime&nbsp;</span><span class="mtk20">import</span><span class="mtk1">&nbsp;datetime</span></span></div><div style="top:138px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:161px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;Email&nbsp;Config&nbsp;----------------</span></span></div><div style="top:184px;height:23px;" class="view-line"><span><span class="mtk1">EMAIL_SENDER&nbsp;=&nbsp;</span><span class="mtk5">"muthwiimeshack@gmail.com"</span></span></div><div style="top:207px;height:23px;" class="view-line"><span><span class="mtk1">EMAIL_PASSWORD&nbsp;=&nbsp;</span><span class="mtk5">"rkubtmzydtgymkrf"</span><span class="mtk1">&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Gmail&nbsp;App&nbsp;Password</span></span></div><div style="top:230px;height:23px;" class="view-line"><span><span class="mtk1">EMAIL_RECEIVER&nbsp;=&nbsp;</span><span class="mtk5">"muthwiimeshack@gmail.com"</span></span></div><div style="top:253px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:276px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;Initialize&nbsp;session&nbsp;state&nbsp;------</span><span class="mtk8">----------</span></span></div><div style="top:299px;height:23px;" class="view-line"><span><span class="mtk20">if</span><span class="mtk1">&nbsp;</span><span class="mtk5">"submissions"</span><span class="mtk1">&nbsp;</span><span class="mtk19">not</span><span class="mtk1">&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;st.session_state</span><span class="mtk14">:</span></span></div><div style="top:322px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.session_state</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">"submissions"</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;pd.DataFrame</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">columns=</span><span class="mtk14 bracket-highlighting-1">[</span></span></div><div style="top:345px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk5">"Name"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Email"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Phone"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Service"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Date&nbsp;&amp;&nbsp;Time"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Submitted&nbsp;At"</span></span></div><div style="top:368px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:391px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:414px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;Sidebar&nbsp;Navigation&nbsp;------------</span><span class="mtk8">----</span></span></div><div style="top:437px;height:23px;" class="view-line"><span><span class="mtk1">st.sidebar.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Thrive&nbsp;Mental&nbsp;Wellness"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:460px;height:23px;" class="view-line"><span><span class="mtk1">page&nbsp;=&nbsp;st.sidebar.radio</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Navigate"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">"Home"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Services"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Staff"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Book&nbsp;Appointment"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Admin"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Legal"</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:483px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:506px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;Custom&nbsp;CSS&nbsp;&amp;&nbsp;Animations&nbsp;-------</span><span class="mtk8">---------</span></span></div><div style="top:529px;height:23px;" class="view-line"><span><span class="mtk1">st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"""</span></span></div><div style="top:552px;height:23px;" class="view-line"><span><span class="mtk5">&lt;link&nbsp;href="</span><span class="mtk5 detected-link">https://fonts.googleapis.com/css2?family=Roboto&amp;fa</span><span class="mtk5 detected-link">mily=Lato&amp;display=swap</span><span class="mtk5">"&nbsp;rel="stylesheet"&gt;</span></span></div><div style="top:575px;height:23px;" class="view-line"><span><span class="mtk5">&lt;style&gt;</span></span></div><div style="top:598px;height:23px;" class="view-line"><span><span class="mtk5">body&nbsp;{&nbsp;font-family:&nbsp;'Roboto',&nbsp;sans-serif;&nbsp;backgrou</span><span class="mtk5">nd-color:#f4f6f7;&nbsp;}</span></span></div><div style="top:621px;height:23px;" class="view-line"><span><span class="mtk5">h1,h2,h3,h4&nbsp;{&nbsp;font-family:&nbsp;'Lato',&nbsp;sans-serif;&nbsp;}</span></span></div><div style="top:644px;height:23px;" class="view-line"><span><span class="mtk5">.hero&nbsp;{&nbsp;background-color:#a0d8f1;&nbsp;padding:50px;&nbsp;bo</span><span class="mtk5">rder-radius:10px;&nbsp;text-align:center;&nbsp;color:#003366</span><span class="mtk5">;&nbsp;animation:&nbsp;fadeIn&nbsp;2s;&nbsp;}</span></span></div><div style="top:667px;height:23px;" class="view-line"><span><span class="mtk5">.card&nbsp;{&nbsp;background-color:white;&nbsp;padding:20px;&nbsp;bord</span><span class="mtk5">er-radius:10px;&nbsp;box-shadow:2px&nbsp;2px&nbsp;12px&nbsp;rgba(0,0,0</span><span class="mtk5">,0.1);&nbsp;margin-bottom:20px;&nbsp;transition:&nbsp;transform&nbsp;0</span><span class="mtk5">.3s;}</span></span></div><div style="top:690px;height:23px;" class="view-line"><span><span class="mtk5">.card:hover&nbsp;{&nbsp;transform:&nbsp;scale(1.03);&nbsp;}</span></span></div><div style="top:713px;height:23px;" class="view-line"><span><span class="mtk5">.card&nbsp;img:hover&nbsp;{&nbsp;transform:&nbsp;scale(1.05);&nbsp;box-shad</span><span class="mtk5">ow:&nbsp;4px&nbsp;4px&nbsp;20px&nbsp;rgba(0,0,0,0.2);}</span></span></div><div style="top:736px;height:23px;" class="view-line"><span><span class="mtk5">button:hover&nbsp;{&nbsp;background-color:&nbsp;#009e8f;&nbsp;transiti</span><span class="mtk5">on:&nbsp;0.3s;&nbsp;}</span></span></div><div style="top:759px;height:23px;" class="view-line"><span><span class="mtk5">a.button:hover&nbsp;{&nbsp;transform:&nbsp;scale(1.05);&nbsp;transitio</span><span class="mtk5">n:&nbsp;0.3s;}</span></span></div><div style="top:782px;height:23px;" class="view-line"><span><span class="mtk5">@keyframes&nbsp;fadeIn&nbsp;{&nbsp;0%&nbsp;{opacity:&nbsp;0;}&nbsp;100%&nbsp;{opacity</span><span class="mtk5">:&nbsp;1;}&nbsp;}</span></span></div><div style="top:805px;height:23px;" class="view-line"><span><span class="mtk5">&lt;/style&gt;</span></span></div><div style="top:828px;height:23px;" class="view-line"><span><span class="mtk5">"""</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:851px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:874px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;HOME&nbsp;PAGE&nbsp;----------------</span></span></div><div style="top:897px;height:23px;" class="view-line"><span><span class="mtk20">if</span><span class="mtk1">&nbsp;page&nbsp;==&nbsp;</span><span class="mtk5">"Home"</span><span class="mtk14">:</span></span></div><div style="top:920px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.image</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"images/thrive_logo.png"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;width=</span><span class="mtk6">200</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:943px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"""</span></span></div><div style="top:966px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&lt;div&nbsp;class='hero'&gt;</span></span></div><div style="top:989px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;h1&gt;🧠&nbsp;Thrive&nbsp;Mental&nbsp;Wellness&nbsp;LLC&lt;/h1&gt;</span></span></div><div style="top:1012px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;p&gt;Comprehensive&nbsp;mental&nbsp;health&nbsp;care&nbsp;in&nbsp;a&nbsp;w</span><span class="mtk5">arm&nbsp;and&nbsp;welcoming&nbsp;environment&lt;/p&gt;</span></span></div><div style="top:1035px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&lt;a&nbsp;href='#appointment'&nbsp;class='button'&nbsp;styl</span><span class="mtk5">e='background-color:#00bfa5;color:white;padding:10</span><span class="mtk5">px&nbsp;20px;border-radius:5px;text-decoration:none;'&gt;B</span><span class="mtk5">ook&nbsp;Appointment&lt;/a&gt;</span></span></div><div style="top:1058px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&lt;/div&gt;</span></span></div><div style="top:1081px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;"""</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1104px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;style='height:50px'&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1127px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Welcome&nbsp;to&nbsp;Thrive&nbsp;Mental&nbsp;Wellness.&nbsp;Our&nbsp;team&nbsp;provi</span><span class="mtk5">des&nbsp;expert&nbsp;psychiatric&nbsp;care,&nbsp;including&nbsp;medication&nbsp;</span><span class="mtk5">management&nbsp;and&nbsp;psychotherapy,&nbsp;tailored&nbsp;to&nbsp;your&nbsp;nee</span><span class="mtk5">ds."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1150px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:1173px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;SERVICES&nbsp;PAGE&nbsp;----------------</span></span></div><div style="top:1196px;height:23px;" class="view-line"><span><span class="mtk20">elif</span><span class="mtk1">&nbsp;page&nbsp;==&nbsp;</span><span class="mtk5">"Services"</span><span class="mtk14">:</span></span></div><div style="top:1219px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Our&nbsp;Services"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1242px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;style='height:20px'&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1265px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;col1</span><span class="mtk14">,</span><span class="mtk1">&nbsp;col2&nbsp;=&nbsp;st.columns</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk6">2</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1288px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">with</span><span class="mtk1">&nbsp;col1</span><span class="mtk14">:</span></span></div><div style="top:1311px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;class='card'&gt;&lt;h3&gt;Medication&nbsp;Management&lt;/h3&gt;&lt;</span><span class="mtk5">p&gt;Comprehensive&nbsp;evaluation&nbsp;and&nbsp;monitoring&nbsp;of&nbsp;psych</span><span class="mtk5">iatric&nbsp;medications.&lt;/p&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1334px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">with</span><span class="mtk1">&nbsp;col2</span><span class="mtk14">:</span></span></div><div style="top:1357px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;class='card'&gt;&lt;h3&gt;Psychotherapy&lt;/h3&gt;&lt;p&gt;Indivi</span><span class="mtk5">dual,&nbsp;group,&nbsp;and&nbsp;family&nbsp;therapy&nbsp;sessions&nbsp;for&nbsp;menta</span><span class="mtk5">l&nbsp;health&nbsp;support.&lt;/p&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1380px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:1403px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;STAFF&nbsp;PAGE&nbsp;----------------</span></span></div><div style="top:1426px;height:23px;" class="view-line"><span><span class="mtk20">elif</span><span class="mtk1">&nbsp;page&nbsp;==&nbsp;</span><span class="mtk5">"Staff"</span><span class="mtk14">:</span></span></div><div style="top:1449px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Meet&nbsp;Our&nbsp;Staff"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1472px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;style='height:20px'&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1495px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:1518px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Upload&nbsp;your&nbsp;photo&nbsp;below&nbsp;(admins/staff&nbsp;only):"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1541px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;uploaded_file&nbsp;=&nbsp;st.file_uploader</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Upload&nbsp;Staff&nbsp;Photo"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk16">type</span><span class="mtk1">=</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">"png"</span><span class="mtk14">,</span><span class="mtk5">"jpg"</span><span class="mtk14">,</span><span class="mtk5">"jpeg"</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1564px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;camera_image&nbsp;=&nbsp;st.camera_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Or&nbsp;take&nbsp;a&nbsp;photo&nbsp;with&nbsp;your&nbsp;camera"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1587px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:1610px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;uploaded_file</span><span class="mtk14">:</span></span></div><div style="top:1633px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.image</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">uploaded_file</span><span class="mtk14">,</span><span class="mtk1">&nbsp;caption=</span><span class="mtk5">"Uploaded&nbsp;Staff&nbsp;Photo"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;use_column_width=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1656px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">elif</span><span class="mtk1">&nbsp;camera_image</span><span class="mtk14">:</span></span></div><div style="top:1679px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.image</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">camera_image</span><span class="mtk14">,</span><span class="mtk1">&nbsp;caption=</span><span class="mtk5">"Captured&nbsp;Photo"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;use_column_width=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1702px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:1725px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;=&nbsp;st.text_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Full&nbsp;Name"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1748px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;role&nbsp;=&nbsp;st.text_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Role&nbsp;/&nbsp;Position"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1771px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;bio&nbsp;=&nbsp;st.text_area</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Short&nbsp;Bio&nbsp;/&nbsp;Specialty"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1794px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:1817px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;st.button</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Save&nbsp;Staff&nbsp;Profile"</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:1840px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;uploaded_file&nbsp;</span><span class="mtk19">or</span><span class="mtk1">&nbsp;camera_image</span><span class="mtk14">:</span></span></div><div style="top:1863px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;img_to_save&nbsp;=&nbsp;uploaded_file&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;uploaded_file&nbsp;</span><span class="mtk20">else</span><span class="mtk1">&nbsp;camera_image</span></span></div><div style="top:1886px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;img_name&nbsp;=&nbsp;</span><span class="mtk10">f</span><span class="mtk5">"</span><span class="mtk14 bracket-highlighting-0">{</span><span class="mtk1">name.replace</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">'&nbsp;'</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">'_'</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">}</span><span class="mtk5">_</span><span class="mtk14 bracket-highlighting-0">{</span><span class="mtk1">datetime.now</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">.strftime</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk5">'%Y%m%d%H%M%S'</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">}</span><span class="mtk5">.png"</span></span></div><div style="top:1909px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">with</span><span class="mtk1">&nbsp;</span><span class="mtk17">open</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"images/</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">img_name</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"wb"</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;f</span><span class="mtk14">:</span></span></div><div style="top:1932px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;f.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">img_to_save.getbuffer</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1955px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"✅&nbsp;Staff&nbsp;profile&nbsp;saved&nbsp;for&nbsp;</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">name</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">&nbsp;(</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">role</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">)"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:1978px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">else</span><span class="mtk14">:</span></span></div><div style="top:2001px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.error</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Please&nbsp;upload&nbsp;a&nbsp;photo&nbsp;or&nbsp;take&nbsp;a&nbsp;photo&nbsp;before&nbsp;savi</span><span class="mtk5">ng"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2024px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:2047px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;APPOINTMENT&nbsp;BOOKING&nbsp;PAGE&nbsp;------</span><span class="mtk8">----------</span></span></div><div style="top:2070px;height:23px;" class="view-line"><span><span class="mtk20">elif</span><span class="mtk1">&nbsp;page&nbsp;==&nbsp;</span><span class="mtk5">"Book&nbsp;Appointment"</span><span class="mtk14">:</span></span></div><div style="top:2093px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"📅&nbsp;Book&nbsp;an&nbsp;Appointment"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2116px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;id='appointment'&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2139px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;class='card'&gt;&lt;p&gt;Please&nbsp;fill&nbsp;the&nbsp;form&nbsp;below&nbsp;a</span><span class="mtk5">nd&nbsp;our&nbsp;staff&nbsp;will&nbsp;contact&nbsp;you&nbsp;to&nbsp;confirm&nbsp;your&nbsp;appo</span><span class="mtk5">intment.&lt;/p&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2162px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:2185px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">with</span><span class="mtk1">&nbsp;st.form</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"appointment_form"</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:2208px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name&nbsp;=&nbsp;st.text_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Full&nbsp;Name"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2231px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;email&nbsp;=&nbsp;st.text_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Email"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2254px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone&nbsp;=&nbsp;st.text_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Phone"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2277px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service&nbsp;=&nbsp;st.selectbox</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Select&nbsp;Service"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">"Medication&nbsp;Management"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"Psychotherapy"</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2300px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;date_time&nbsp;=&nbsp;st.date_input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Preferred&nbsp;Date"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2323px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;submit&nbsp;=&nbsp;st.form_submit_button</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Submit&nbsp;Appointment"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2346px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:2369px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;submit</span><span class="mtk14">:</span></span></div><div style="top:2392px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;submitted_at&nbsp;=&nbsp;datetime.now</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">.strftime</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"%Y-%m-%d&nbsp;%H:%M:%S"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2415px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.session_state.submissions.loc</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk17">len</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">st.session_state.submissions</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk1">name</span><span class="mtk14">,</span><span class="mtk1">&nbsp;email</span><span class="mtk14">,</span><span class="mtk1">&nbsp;phone</span><span class="mtk14">,</span><span class="mtk1">&nbsp;service</span><span class="mtk14">,</span><span class="mtk1">&nbsp;date_time</span><span class="mtk14">,</span><span class="mtk1">&nbsp;submitted_at</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top:2438px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.success</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"✅&nbsp;Appointment&nbsp;submitted&nbsp;successfully!"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2461px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">try</span><span class="mtk14">:</span></span></div><div style="top:2484px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg_content&nbsp;=&nbsp;f\</span><span class="mtk5">"\"\"New&nbsp;Appointment&nbsp;Submission\\nName:&nbsp;{name}\\nE</span><span class="mtk5">mail:&nbsp;{email}\\nPhone:&nbsp;{phone}\\nService:&nbsp;{service</span><span class="mtk5">}\\nDate:&nbsp;{date_time}\\nSubmitted&nbsp;At:&nbsp;{submitted_a</span><span class="mtk5">t}\"\"\"</span></span></div><div style="top:2507px;height:23px;" class="view-line"><span><span class="mtk5">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg&nbsp;=&nbsp;MIMEText(msg_content)</span></span></div><div style="top:2530px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">"Subject"</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;</span><span class="mtk5">"New&nbsp;Appointment&nbsp;Submission&nbsp;-&nbsp;Thrive&nbsp;Mental&nbsp;Wellne</span><span class="mtk5">ss"</span></span></div><div style="top:2553px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">"From"</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;EMAIL_SENDER</span></span></div><div style="top:2576px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;msg</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">"To"</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;EMAIL_RECEIVER</span></span></div><div style="top:2599px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">with</span><span class="mtk1">&nbsp;smtplib.SMTP_SSL</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"smtp.gmail.com"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk6">465</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;server</span><span class="mtk14">:</span></span></div><div style="top:2622px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server.login</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">EMAIL_SENDER</span><span class="mtk14">,</span><span class="mtk1">&nbsp;EMAIL_PASSWORD</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2645px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server.send_message</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">msg</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2668px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.info</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"📧&nbsp;Notification&nbsp;sent&nbsp;to&nbsp;clinic&nbsp;email."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2691px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">except</span><span class="mtk1">&nbsp;Exception&nbsp;</span><span class="mtk20">as</span><span class="mtk1">&nbsp;e</span><span class="mtk14">:</span></span></div><div style="top:2714px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.error</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"❌&nbsp;Email&nbsp;failed:&nbsp;</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">e</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2737px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:2760px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;ADMIN&nbsp;PAGE&nbsp;----------------</span></span></div><div style="top:2783px;height:23px;" class="view-line"><span><span class="mtk20">elif</span><span class="mtk1">&nbsp;page&nbsp;==&nbsp;</span><span class="mtk5">"Admin"</span><span class="mtk14">:</span></span></div><div style="top:2806px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Admin&nbsp;Dashboard"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2829px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.markdown</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"&lt;div&nbsp;style='height:20px'&gt;&lt;/div&gt;"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;unsafe_allow_html=</span><span class="mtk9">True</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2852px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"View&nbsp;all&nbsp;appointment&nbsp;submissions"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2875px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.dataframe</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">st.session_state.submissions</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2898px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;csv&nbsp;=&nbsp;st.session_state.submissions.to_csv</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">index=</span><span class="mtk9">False</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">.encode</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">'utf-8'</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2921px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.download_button</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Download&nbsp;CSV"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;data=csv</span><span class="mtk14">,</span><span class="mtk1">&nbsp;file_name=</span><span class="mtk5">"appointments.csv"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:2944px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span></span></div><div style="top:2967px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;</span><span class="mtk19">not</span><span class="mtk1">&nbsp;st.session_state.submissions.empty</span><span class="mtk14">:</span></span></div><div style="top:2990px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.subheader</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Appointment&nbsp;Analytics"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3013px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;df&nbsp;=&nbsp;st.session_state.submissions</span></span></div><div style="top:3036px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Total&nbsp;Appointments:"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk17">len</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3059px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.bar_chart</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Service'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk1">.value_counts</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3082px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;df</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">'Submitted&nbsp;At'</span><span class="mtk14 bracket-highlighting-0">]</span><span class="mtk1">&nbsp;=&nbsp;pd.to_datetime</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Submitted&nbsp;At'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3105px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;st.line_chart</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">df.groupby</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">df</span><span class="mtk14 bracket-highlighting-2">[</span><span class="mtk5">'Submitted&nbsp;At'</span><span class="mtk14 bracket-highlighting-2">]</span><span class="mtk1">.dt.date</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-1">[</span><span class="mtk5">'Name'</span><span class="mtk14 bracket-highlighting-1">]</span><span class="mtk1">.count</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3128px;height:23px;" class="view-line"><span><span></span></span></div><div style="top:3151px;height:23px;" class="view-line"><span><span class="mtk8">#&nbsp;----------------&nbsp;LEGAL&nbsp;PAGE&nbsp;----------------</span></span></div><div style="top:3174px;height:23px;" class="view-line"><span><span class="mtk20">elif</span><span class="mtk1">&nbsp;page&nbsp;==&nbsp;</span><span class="mtk5">"Legal"</span><span class="mtk14">:</span></span></div><div style="top:3197px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.title</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Legal&nbsp;Information"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3220px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.subheader</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Privacy&nbsp;Policy"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3243px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"All&nbsp;patient&nbsp;data&nbsp;is&nbsp;kept&nbsp;confidential&nbsp;and&nbsp;stored&nbsp;</span><span class="mtk5">securely.&nbsp;HIPAA&nbsp;compliance&nbsp;is&nbsp;maintained&nbsp;at&nbsp;all&nbsp;ti</span><span class="mtk5">mes."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3266px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.subheader</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Terms&nbsp;of&nbsp;Service"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3289px;height:23px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;st.write</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Use&nbsp;of&nbsp;this&nbsp;site&nbsp;constitutes&nbsp;agreement&nbsp;to&nbsp;our&nbsp;ter</span><span class="mtk5">ms.&nbsp;Appointments&nbsp;are&nbsp;subject&nbsp;to&nbsp;clinic&nbsp;policies."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:3312px;height:23px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 23px; top: 3312px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 18px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 23px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="visible scrollbar horizontal" style="position: absolute; width: 1185px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 750px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="3345" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 3345px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 3345px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 3345px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1205px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 39.5938px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 18px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 23px; letter-spacing: 0px; top: 3312px; left: 6px; width: 98984px; height: 1px;"></textarea><div style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;" class="monaco-editor-background textAreaCover"></div><div data-mprt="4" class="overlayWidgets" style="width: 1205px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 3345px;"><div class="minimap-shadow-hidden" style="height: 3345px;"></div><canvas width="0" height="3345" style="position: absolute; left: 0px; width: 0px; height: 3345px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="3345" style="position: absolute; left: 0px; width: 0px; height: 3345px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1366px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 18px; line-height: 1.27778; max-width: 795.3px; max-height: 836.25px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content" hidden="">
          <div class="output-info"> </div>
          <div class="output-iframe-container" hidden="">
            <div class="output-iframe-sizer"> <div><div></div></div></div>
          </div>
        </div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$065098016$--> <div class="footer-links" style="padding-bottom: 66px;">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$065098016$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$065098016$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow" style="box-shadow: rgba(0, 0, 0, 0.15) 0px 4px 4px -2px inset;"></div>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$065098016$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$065098016$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-2-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-2-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$065098016$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$065098016$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$065098016$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$065098016$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-1-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-1-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$065098016$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$065098016$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$065098016$--><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" id="tab-pane-3-more-actions-button" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->more_horiz</md-icon>
    </md-icon-button>
    <colab-tooltip-trigger aria-hidden="true" for="tab-pane-3-more-actions-button" message="More tab actions"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->More tab actions</div><!----><!--?--></template>
    </colab-tooltip-trigger><!--?lit$065098016$-->
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./4app_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./4app_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-composer view-mode="floating" style="transform: translate(0px, 0px);"><template shadowrootmode="open"><!---->
      <colab-composer-conversation><template shadowrootmode="open"><!---->
      <div class="scrollable">
        <!--?lit$065098016$-->
        <!--?lit$065098016$-->
      </div>
    </template>
      </colab-composer-conversation>
      <!--?lit$065098016$-->
      <div class="footer">
        <!--?lit$065098016$--> <!--?lit$065098016$-->
        <div class="input-container">
          <colab-composer-input><template shadowrootmode="open"><!---->
      <div class="wrapper">
        <!--?lit$065098016$-->
        <!--?lit$065098016$-->
              <div class="text-field-and-spark">
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$065098016$-->
          <div class="text-field-wrapper" data-value="">
            <md-outlined-text-field type="textarea" aria-controls="autocomplete-menu" rows="1" data-aria-autocomplete="list" class="composer-input-field" data-aria-expanded="false" maxlength="2000" placeholder="What can I help you build?" inputmode="" autocomplete=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <span class="text-field  textarea ">
        <!--?lit$065098016$--><md-outlined-field class="field" count="0" error-text="" label="" max="2000" resizable="" supporting-text=""><template shadowrootmode="open"><!---->
      <div class="field  resizable no-label ">
        <div class="container-overflow">
          <!--?lit$065098016$-->
          <slot name="container"></slot>
          <!--?lit$065098016$--> <!--?lit$065098016$--> <!--?lit$065098016$-->
      <div class="outline">
        <div class="outline-start"></div>
        <div class="outline-notch">
          <div class="outline-panel-inactive"></div>
          <div class="outline-panel-active"></div>
          <div class="outline-label"><!--?lit$065098016$--></div>
        </div>
        <div class="outline-end"></div>
      </div>
    
          <div class="container">
            <div class="start">
              <slot name="start"></slot>
            </div>
            <div class="middle">
              <div class="label-wrapper">
                <!--?lit$065098016$--> <!--?lit$065098016$-->
              </div>
              <div class="content">
                <slot></slot>
              </div>
            </div>
            <div class="end">
              <slot name="end"></slot>
            </div>
          </div>
        </div>
        <!--?lit$065098016$-->
      <div class="supporting-text"><!--?lit$065098016$--><span><!--?lit$065098016$--></span><!--?lit$065098016$--><span class="counter"><!--?lit$065098016$-->0 / 2000</span></div>
      <slot name="aria-describedby"></slot>
    
      </div>
    </template>
      <!--?lit$065098016$-->
      <span class="icon leading" slot="start">
        <slot name="leading-icon"></slot>
      </span>
    
      <!--?lit$065098016$-->
        <textarea class="input" aria-describedby="description" aria-invalid="false" maxlength="2000" placeholder="What can I help you build?" rows="1" cols="20"></textarea>
      
      <!--?lit$065098016$-->
      <span class="icon trailing" slot="end">
        <slot name="trailing-icon"></slot>
      </span>
    
      <div id="description" slot="aria-describedby" hidden=""><!----><!--?lit$065098016$--> <!--?lit$065098016$-->0 / 2000<!--?--></div>
      <slot name="container" slot="container"></slot>
    </md-outlined-field>
      </span>
    </template>
            </md-outlined-text-field>
            <!--?lit$065098016$-->
          </div>
        
              </div>
              <div class="actions">
                <!--?lit$065098016$--><md-icon-button data-aria-haspopup="true" id="add-context" data-aria-label="Add to Gemini" data-aria-expanded="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add to Gemini" aria-haspopup="true" aria-expanded="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add_circle</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="add-context" message="Add to Gemini"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Add to Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <md-menu positioning="popover" quick="" aria-labelledby="add-context" anchor="add-context" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$065098016$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$065098016$--><slot></slot> </div>
        </div>
      </div>
    </template>
        <!--?lit$065098016$-->
      <md-menu-item md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <md-icon slot="start" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>folder</md-icon>
        <span slot="headline"><!--?lit$065098016$-->Select files</span>
      </md-menu-item>
      <md-menu-item md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$065098016$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$065098016$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$065098016$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$065098016$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
        <md-icon slot="start" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>upload</md-icon>
        <span slot="headline"><!--?lit$065098016$-->Upload</span>
      </md-menu-item>
    
        <!--?lit$065098016$-->
      </md-menu>
                <!--?lit$065098016$--><md-icon-button id="send" data-aria-label="Send" aria-describedby="send-tooltip" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Send" aria-disabled="true">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>send</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="send" id="send-tooltip" message="Send"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Send</div><!----><!--?--></template>
      </colab-tooltip-trigger>
              </div>
            
      </div>
      <!--?lit$065098016$-->
      <input type="file" hidden="" multiple="">
    </template></colab-composer-input>
          <!--?lit$065098016$--><div class="floating-actions">
      <!--?lit$065098016$--><!--?lit$065098016$-->
      <md-icon-button id="move-to-side-panel" data-aria-label="Move to panel" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move to panel">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>dock_to_left</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="move-to-side-panel" message="Move to panel"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Move to panel</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    <!--?lit$065098016$--><md-icon-button id="close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="close" message="Close"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Close</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?-->
    </div>
        </div>
        <!--?lit$065098016$--> <!--?lit$065098016$-->
      </div>
      <!--?lit$065098016$-->
    
    </template></colab-composer><colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="middle"><!--?lit$065098016$-->
      <md-icon-button toggle="" id="toggle-composer" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$065098016$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$065098016$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$065098016$--><span class="icon"><slot></slot></span>
        <!--?lit$065098016$-->
        <!--?lit$065098016$--><span class="touch"></span>
  </button></template>
        <!--?lit$065098016$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$065098016$--><!----><div><!--?lit$065098016$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </span>
      <span class="right">
        <!--?lit$065098016$--><colab-execution-status><template shadowrootmode="open"><!----></template></colab-execution-status><!--?lit$065098016$--><!--?lit$065098016$--><!--?lit$065098016$--><colab-runtime-status><template shadowrootmode="open"><!----></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->data_object</md-icon>
        <!--?lit$065098016$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$065098016$-->terminal</md-icon>
        <!--?lit$065098016$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Locate in Drive<!--?lit$065098016$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Open in playground mode<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->New notebook in Drive<!--?lit$065098016$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Open notebook<!--?lit$065098016$--></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Upload notebook<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Rename<!--?lit$065098016$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Move<!--?lit$065098016$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Move to the bin<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Save a copy in Drive<!--?lit$065098016$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Save a copy as a GitHub Gist<!--?lit$065098016$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Save a copy in GitHub<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Save<!--?lit$065098016$--></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Save and pin revision<!--?lit$065098016$--></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Revision history<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$065098016$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Print<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Download .ipynb<!--?lit$065098016$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Download .py<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Undo<!--?lit$065098016$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Redo<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Select all cells<!--?lit$065098016$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Cut cell or selection<!--?lit$065098016$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Copy cell or selection<!--?lit$065098016$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Paste<!--?lit$065098016$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Delete selected cells<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Find and replace<!--?lit$065098016$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Find next<!--?lit$065098016$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Find previous<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Notebook settings<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Clear all outputs<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$065098016$-->Table of contents<!--?lit$065098016$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Notebook info<!--?lit$065098016$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Executed code history<!--?lit$065098016$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Start slideshow<!--?lit$065098016$--></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Start slideshow from beginning<!--?lit$065098016$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$065098016$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1g" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Collapse sections<!--?lit$065098016$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Expand sections<!--?lit$065098016$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Save collapsed section layout<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1k" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Show/hide code<!--?lit$065098016$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Show/hide output<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1n" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Focus next tab<!--?lit$065098016$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Focus previous tab<!--?lit$065098016$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Move tab to next pane<!--?lit$065098016$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Move tab to previous pane<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Hide comments<!--?lit$065098016$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Minimise comments<!--?lit$065098016$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Expand comments<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Code cell<!--?lit$065098016$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Text cell<!--?lit$065098016$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Section header cell<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1w" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Scratch code cell<!--?lit$065098016$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Code snippets<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Add a form field<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Run all<!--?lit$065098016$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Run before<!--?lit$065098016$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Run the focused cell<!--?lit$065098016$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Run selection<!--?lit$065098016$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Run cell and below<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Interrupt execution<!--?lit$065098016$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Restart session<!--?lit$065098016$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Restart session and run all<!--?lit$065098016$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Disconnect and delete runtime<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Change runtime type<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2e" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Manage sessions<!--?lit$065098016$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->View resources<!--?lit$065098016$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->View runtime logs<!--?lit$065098016$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Command palette<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2k" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Settings<!--?lit$065098016$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Keyboard shortcuts<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2n" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Diff notebooks<!--?lit$065098016$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$065098016$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$065098016$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Frequently asked questions<!--?lit$065098016$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->View release notes<!--?lit$065098016$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Search code snippets<!--?lit$065098016$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2t" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Report a bug<!--?lit$065098016$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Report Drive abuse<!--?lit$065098016$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->Send feedback<!--?lit$065098016$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->View Terms of Service<!--?lit$065098016$--></div></div><div command="view-in-english" class=" goog-menuitem " role="menuitem" id=":2y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$065098016$-->View in English<!--?lit$065098016$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$065098016$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$065098016$--><button id="button" class="button">
      <!--?lit$065098016$-->
      <span class="touch"></span>
      <!--?lit$065098016$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$065098016$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$065098016$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy788a7c9dc68e756eb2da844404158205b0e0c41a0.2116688948" name="apiproxy788a7c9dc68e756eb2da844404158205b0e0c41a0.2116688948" src="./4app_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><iframe src="./4app_files/bscframe.html" style="display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-pne9bvtn26ic" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./4app_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;"></textarea></div><iframe style="display: none;" src="./4app_files/saved_resource.html"></iframe></div></body></html>