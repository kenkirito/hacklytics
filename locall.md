<h1 align="center"><strong> Guidelines</strong></h1>

---

<h2 align="center"><b>How to make a Pull Request? 👇</b></h2>


**1.** Fork [this](https://github.com/kenkirito/hacklytics) repository.

**2.** Clone your forked copy of the project.

```
git clone https://github.com/<your_user_name>/hacklytics.git
```

**3.** Navigate to the project directory :file_folder: .

```
cd filterbubbles
```

**4.** Add a reference to the original repository.

```
git remote add upstream https://github.com/kenkirito/hacklytics.git
```

**5.** Check the remotes for this repository.

```
git remote -v
```

**6.** Always take a pull from the upstream repository to your master branch to keep it at par with the main project(updated repository).

```
git pull upstream main
```

**7.** Create a new branch.

```
git checkout -b <your_branch_name>
```

**8.** Perform your desired changes to the code base.


**9.** Stage your changes .

```
git add .
```

**10.** Commit your changes ✅.

```
git commit -m "Relevant message"
```

**11.** Push the committed changes in your feature branch to your remote repo.

```
git push -u origin <your_branch_name>
```

**12.** To create a pull request, click on `compare and pull requests`. Please ensure you compare your feature branch to the desired branch of the repo you are suppose to make a PR to.

**13.** Then add an appropriate title and description to your pull request that explains your changes and efforts done.

**14.** Click on `Create Pull Request`.

**15.** hola for making first pull request
