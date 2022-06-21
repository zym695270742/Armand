<template>
  <div>
      <el-container>
          <el-form :model="proj_details" label-width="120px">
              <el-form-item label="项目名称">
                  <el-input v-model="proj_details.proj_name"></el-input>
              </el-form-item>
              <el-form-item label="项目描述">
                  <el-input type="textarea" v-model="proj_details.des"></el-input>
              </el-form-item>

              <el-form :model="proj_details" label-width="120px" :disabled="true">
                <el-form-item label="项目创建者">
                    <el-input v-model="proj_details.creator"></el-input>
                </el-form-item>
                <el-form-item label="项目创建时间">
                    <el-input type="datetime" v-model="proj_details.create_time"></el-input>
                </el-form-item>
                <el-form-item label="项目更新者">
                    <el-input v-model="proj_details.updator"></el-input>
                </el-form-item>
                <el-form-item label="项目更新时间">
                    <el-input type="datetime" v-model="proj_details.update_time"></el-input>
                </el-form-item>
              </el-form>
          </el-form>
      </el-container>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: "Proj_config",
  data(){
    return{
      proj_details:{
        proj_name: 'www',
        des: 'wwww',
        creator: 'carol',
        create_time: '2002-09-09 16:00:00',
        updator: 'lisia',
        update_time: '2022-06-09 06:00:00',
      }
    }
  },
  methods:{

  },
  mounted:function(){
    axios.get('http://localhost:8000/get_proj_config/',{
      params:{
        proj_id: this.proj_id,
      }
    }).then(
        res=>this.proj_details = res.data
    )
  },
  props:['proj_id'],
}
</script>

<style scoped>

</style>