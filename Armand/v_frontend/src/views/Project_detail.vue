<template>
<div style="height: 100%;">
  <el-container style="height: 100%;">
    <el-aside width="200px">
      <Menu></Menu>
    </el-aside>
    <el-container>
      <el-header style="line-height: 60px;">
          <span> Porject ID: {{$route.query.proj_id}}</span>
      </el-header>
      <el-main>

        <h2>详情页</h2>

      </el-main>
    </el-container>
  </el-container>
</div>
</template>

<script>
import Menu from '../components/Menu.vue'
import axios from 'axios'
export default {
  name: "project_detail",
  data(){
    return{

    }
  },
  methods:{

  },
  components:{
    Menu,
  },
  mounted:function(){

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