<template>
    <el-menu
      default-active="2"
      class="el-menu-vertical-demo"
      router
      :default-openeds="['1','2']">

      <el-menu-item index="/">首页Home</el-menu-item>
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>功能区</span>
        </template>
        <el-menu-item index="1-1-1">项目管理</el-menu-item>
        <el-menu-item index="1-1-2">环境管理</el-menu-item>
        <el-menu-item index="1-1-3">官方接口库</el-menu-item>
        <el-menu-item index="1-1-4">线上监控</el-menu-item>
        <el-menu-item-group>
          <template slot="title">接口导入</template>
          <el-menu-item index="1-5-1">接口文档</el-menu-item>
          <el-menu-item index="1-5-2">Postman</el-menu-item>
          <el-menu-item index="1-5-3">在线抓包</el-menu-item>
          <el-menu-item index="1-5-4">其他</el-menu-item>
        </el-menu-item-group>

      </el-submenu>
      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-user-solid"></i>
          <span>用户区</span>
        </template>
        <el-menu-item index="2-1-1">个人资料</el-menu-item>
        <el-menu-item index="2-2-1">个人贡献</el-menu-item>
        <el-menu-item index="2-3-1">发送消息</el-menu-item>
        <el-menu-item index="help">帮助</el-menu-item>
<!--        <a href="http://localhost:8000/help/"><el-menu-item >帮助</el-menu-item></a>-->
        <a href="http://localhost:8000/logout/"><el-menu-item index="2-4-1">退出</el-menu-item></a>
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-s-tools"></i>
          <span>维护区</span>
        </template>
        <a href="http://localhost:8000/admin/"><el-menu-item >进入后台</el-menu-item></a>
        <el-menu-item index="3-2-1">用户管理</el-menu-item>
        <el-menu-item index="3-3-1">查看日志</el-menu-item>
        <el-menu-item index="3-4-1">发布公告</el-menu-item>
        <el-menu-item index="3-5-1">权限管理</el-menu-item>
      </el-submenu>

    </el-menu>
</template>

<script>
export default {
  name: 'Menu',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 a{
   text-decoration: none;
 }
</style>
