<template>
    <div>
          <el-form :model="proj_details" label-width="100px" label-position="left">
              <el-form-item label="项目名称">
                  <el-input v-model="proj_details.proj_name"></el-input>
              </el-form-item>
              <el-form-item label="项目描述">
                  <el-input type="textarea" v-model="proj_details.des"></el-input>
              </el-form-item>
              <el-form-item label="mock类型">
                  <el-select v-model="proj_details.mock_type" placeholder="请选择" style="width: 100%;" >
                      <el-option label="mock data" name="type1"></el-option>
                      <el-option value="mock 3rd" name="type2"></el-option>
                  </el-select>
              </el-form-item>
              <el-form-item label="保密项目">
                  <el-switch v-model="proj_details.private" style="float: left;display: inline-block;"></el-switch>
              </el-form-item>
              <el-form-item label="测试组">
                  <el-select v-model="proj_details.Group" placeholder="请选择" style="width: 100%;">
                      <el-option label="终端测试组" name="group1"></el-option>
                      <el-option label="系统测试组" name="group2"></el-option>
                  </el-select>
              </el-form-item>
              <el-form-item label="权限设置">
                  <el-checkbox-group v-model="proj_details.Permission" style="float: left">
                        <el-checkbox label="Me" type="Permission"></el-checkbox>
                        <el-checkbox label="Teammates" type="Permission"></el-checkbox>
                        <el-checkbox label="Leader" type="Permission"></el-checkbox>
                        <el-checkbox label="All" type="Permission"></el-checkbox>
                  </el-checkbox-group>
              </el-form-item>
              <el-form-item label="登录变量">
                <el-input type="textarea" v-model="proj_details.Logon_var" :rows='3'></el-input>
              </el-form-item>
              <el-form-item label="公共变量">
                  <el-input type="textarea" v-model="proj_details.Public_var" :rows='3'></el-input>
              </el-form-item>
              <el-form-item label="签名设置" >
                  <el-input type="textarea" v-model="proj_details.sign" :rows='3'></el-input>
              </el-form-item>

              <el-form :model="proj_details" label-width="100px" :disabled="true">
                <el-form-item label="创建者">
                    <el-input v-model="proj_details.creator"></el-input>
                </el-form-item>
                <el-form-item label="创建时间">
                    <el-input type="datetime" v-model="proj_details.create_time"></el-input>
                </el-form-item>
                <el-form-item label="更新者">
                    <el-input v-model="proj_details.updator"></el-input>
                </el-form-item>
                <el-form-item label="更新时间">
                    <el-input type="datetime" v-model="proj_details.update_time"></el-input>
                </el-form-item>
              </el-form>

              <el-from>
                  <el-form-item>
                      <el-button type="primary" @click="updateProjConfig">更新</el-button>
                  </el-form-item>
              </el-from>
          </el-form>
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
        mock_type: '',
        private: false,
        Group: '',
        Logon_var: 'nnn',
        Public_var: 'nnn',
        Permission: [],
        sign: '444444',
      }
    }
  },
  methods:{
    updateProjConfig(){
      axios.post('http://localhost:8000/update_proj_config/', this.proj_details).then(
          this.$message(
              {
                message: 'Update success!',
                type: 'success'
              }
          )
      )
    },
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