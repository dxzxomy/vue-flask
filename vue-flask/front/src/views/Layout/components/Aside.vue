<template>
    <el-menu
      default-active="/"
      class="el-menu-vertical-demo"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      :collapse="isCollapse"
      router
    >
      <el-menu-item index="/">
        <i class="el-icon-menu"></i>
        <span slot="title">首页</span>
      </el-menu-item>
      <el-submenu index="1">
        <template slot="title">
            <i class="el-icon-location"></i>
            <span>交换机模板配置</span>
        </template>
        <el-menu-item index="/switch/switchselect">模板配置查询</el-menu-item>
        <el-menu-item index="/switch/switchmodify">模板配置修改</el-menu-item>
      </el-submenu>
      <el-menu-item index="/image">
        <i class="el-icon-setting"></i>
        <span slot="title">素材管理</span>
      </el-menu-item>
      <el-menu-item index="/publish">
        <i class="el-icon-setting"></i>
        <span slot="title">发布文章</span>
      </el-menu-item>
            <el-menu-item index="/comment">
        <i class="el-icon-setting"></i>
        <span slot="title">评论管理</span>
      </el-menu-item>
            <el-menu-item index="/fans">
        <i class="el-icon-setting"></i>
        <span slot="title">粉丝管理</span>
      </el-menu-item>
            <el-menu-item index="/settings">
        <i class="el-icon-setting"></i>
        <span slot="title">个人设置</span>
      </el-menu-item>
    </el-menu>
</template>

<script>
  export default {
    name: "Aside",
    props: ["isCollapse"],
  }
</script>

<style scoped>
    /*.el-menu-vertical-demo {*/
    /*    transition: 0s width ease-in-out, 0s padding-left ease-in-out, 0s padding-right ease-in-out;*/
    /*}*/

  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    height: 100%;
  }
</style>