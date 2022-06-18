<template>
<div style="height: 100%;">
  <el-container style="height: 100%;">
    <el-aside width="200px">
      <Menu></Menu>
    </el-aside>
    <el-container>
      <el-header></el-header>
      <el-main>
        <h3>这是项目列表</h3>
      </el-main>
    </el-container>
  </el-container>
</div>
</template>

<script>
import Menu from '../components/Menu.vue'
export default {
  name: "project_list",
  components:{
    Menu,
  }
}
</script>

<style scoped>
  .el-header {
    background: linear-gradient(to right, #fbc2eb 0%, #a6c1ee 100%);
    color: #333;
    text-align: center;
    line-height: 15px;
  }

  .el-aside {
    background: linear-gradient(to left, #fbc2eb 0%, #a6c1ee 100%);
    color: #333;
  }

  .el-main {
    color: #333;
  }


  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }

</style>